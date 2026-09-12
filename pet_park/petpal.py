"""
PetPal - a little Python playground where your code brings a pet to life.

You do NOT need to read or change this file. It is the "engine" that draws
your pet on the screen. You write your code in the session files.

Made for the PetPal course.
"""

import sys
import os
import math
import random
import difflib

try:
    import tkinter as tk
    from tkinter import simpledialog
    from tkinter import font as tkfont
except ImportError:  # pragma: no cover
    print("\n  Oh no! Python on this computer is missing 'tkinter'.")
    print("  Ask your teacher for help - on Mac/Windows it usually comes")
    print("  with Python; on Linux run:  sudo apt install python3-tk\n")
    raise


# --------------------------------------------------------------------------
#  Colours your pet can be
# --------------------------------------------------------------------------

COLORS = {
    "golden": "#F2B95C", "gold": "#F2B95C", "cream": "#F7DFB8",
    "peach": "#FFC39B", "pink": "#FFB0C6", "rose": "#F58FA8",
    "lavender": "#C9B6EC", "purple": "#AC8CE3", "sky": "#9BD3F5",
    "blue": "#86B6F0", "mint": "#A6E5CB", "green": "#8ED9A4",
    "grey": "#C6CCD7", "gray": "#C6CCD7", "silver": "#DDE2EA",
    "chocolate": "#B37C55", "brown": "#C69064", "ginger": "#F09A54",
    "white": "#FBFBFB", "black": "#6A6473", "orange": "#FFA65C",
    "yellow": "#FFDE6B", "red": "#FF8E88", "rainbow": "#FFB0C6",
}

MOODS = ("happy", "excited", "sleepy", "sad", "hungry", "surprised")

# Palette for the window
BG = "#FFF7EC"
PANEL = "#FFFFFF"
INK = "#4A4458"
SOFT = "#9A93A8"
ACCENT = "#FF8FB1"
ACCENT2 = "#7FC8F8"
LINE = "#EFE6DA"
BTN_TEXT = "#2F2B38"     # near-black, so button labels are readable everywhere

TYPE_COLORS = {
    "str": ("#FFE3EC", "#D14D74"),
    "int": ("#DCEDFF", "#2F6FB5"),
    "float": ("#E8E0FF", "#6A4BC0"),
    "bool": ("#DFF6E4", "#2E8B57"),
    "list": ("#FFEAD1", "#C4731A"),
    "dict": ("#FFF3C4", "#96700B"),
    "NoneType": ("#EDEDED", "#777777"),
}

W, H = 540, 430          # scene size
GROUND = 336             # y of the ground
TILE0, TILEW = 76, 58    # stepping stones
NTILES = 7
FPS_MS = 33


def _shade(hex_color, factor):
    """Make a colour lighter (factor > 1) or darker (factor < 1)."""
    hex_color = hex_color.lstrip("#")
    r, g, b = (int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
    f = lambda v: max(0, min(255, int(v * factor)))
    return "#%02X%02X%02X" % (f(r), f(g), f(b))


def _resolve_color(value):
    if not isinstance(value, str):
        return COLORS["golden"]
    v = value.strip().lower()
    if v in COLORS:
        return COLORS[v]
    if v.startswith("#") and len(v) in (4, 7):
        return value
    return COLORS["golden"]


# --------------------------------------------------------------------------
#  Kid-friendly error messages
# --------------------------------------------------------------------------

def _friendly(exc):
    name = type(exc).__name__
    msg = str(exc)
    if isinstance(exc, TypeError) and "concatenate" in msg:
        return ("You tried to glue a word and a number together with +.\n"
                "Python needs them to be the same type. Try an f-string:\n"
                '    pet.say(f"I am {pet.age} years old")')
    if isinstance(exc, TypeError) and "unsupported operand" in msg:
        return ("Those two things can't be combined with that maths symbol.\n"
                "Check the types in the Variables panel - is one a str?")
    if isinstance(exc, NameError):
        return ("Python has never heard of that name.\n"
                "Check the spelling, or make sure you created it first.\n"
                "(Remember: names are case sensitive - Name and name differ.)")
    if isinstance(exc, AttributeError) and "Pet" in msg:
        return ("Your pet doesn't know that trick yet.\n"
                "Type  help_me()  in your main() to see everything a pet can do.")
    if isinstance(exc, ValueError) and "invalid literal for int" in msg:
        return ("You asked Python to turn something into a whole number,\n"
                "but it wasn't a number. int(\"3\") works, int(\"three\") does not.")
    if isinstance(exc, IndexError):
        return ("You asked for an item that isn't in the list.\n"
                "Remember the first item is number 0, not 1!")
    if isinstance(exc, ZeroDivisionError):
        return "You can't divide by zero - not even Python knows that answer."
    if isinstance(exc, TypeError) and "argument" in msg:
        return ("That command wanted a different number of things in its ( ).\n"
                "For example pet.walk(3) needs one number inside the brackets.")
    return "%s: %s" % (name, msg)


# --------------------------------------------------------------------------
#  The Pet
# --------------------------------------------------------------------------

_PUBLIC_DEFAULTS = {
    "name": "Unnamed",
    "age": 1,
    "size": 1.0,
    "color": "golden",
    "is_hungry": False,
    "mood": "happy",
}

_TRICKS = ["say", "think", "step", "walk", "back", "turn", "jump", "spin",
           "dance", "wag", "eat", "sleep", "wake", "birthday", "grow",
           "shrink", "wait", "cheer", "sit"]


class Pet:
    """Your electronic pet!

    pet = Pet("dog")     # or Pet("cat")
    """

    def __init__(self, kind="dog"):
        object.__setattr__(self, "_ready", False)
        k = str(kind).strip().lower()
        self.__dict__["kind"] = "cat" if k.startswith("c") else "dog"
        for key, val in _PUBLIC_DEFAULTS.items():
            self.__dict__[key] = val
        # visual state (used by the engine while your program replays)
        self.__dict__["_v"] = {
            "tile": 0.0, "size": 1.0, "facing": 1, "bob": 0.0, "lean": 0.0,
            "legs": 0.0, "tail": 0.0, "blink": 0.0, "eyes": "open",
            "mouth": "smile", "asleep": False, "bubble": None,
            "bubble_kind": "say", "y_off": 0.0, "squash": 1.0, "spin": 0.0,
            "bowl": 0.0, "cake": 0.0, "age": 1, "name": "Unnamed",
            "color": "golden", "hungry": False, "mood": "happy", "lane": 0,
        }
        object.__setattr__(self, "_ready", True)
        STAGE.register(self)

    # -- attribute magic: setting a variable shows up in the Variables panel
    def __setattr__(self, key, value):
        if key.startswith("_") or not self.__dict__.get("_ready", False):
            object.__setattr__(self, key, value)
            return
        if key == "size":
            try:
                value = float(value)
            except (TypeError, ValueError):
                pass
        self.__dict__[key] = value
        STAGE.push({"kind": "set", "pet": self, "key": key, "value": value},
                   line=_caller_line())

    def __repr__(self):
        return "<%s named %s, age %s>" % (self.kind, self.name, self.age)

    def __getattr__(self, key):
        if key.startswith("_"):
            raise AttributeError(key)
        close = difflib.get_close_matches(key, _TRICKS + list(_PUBLIC_DEFAULTS), n=1)
        hint = (" Did you mean '%s'?" % close[0]) if close else ""
        raise AttributeError("Pet has no trick called '%s'.%s" % (key, hint))

    # ---------------- tricks ----------------
    def _act(self, kind, **kw):
        kw.update({"kind": kind, "pet": self})
        STAGE.push(kw, line=_caller_line())

    def say(self, *parts):
        text = " ".join(str(p) for p in parts)
        self._act("say", text=text)

    def think(self, *parts):
        text = " ".join(str(p) for p in parts)
        self._act("say", text=text, bubble="think")

    def step(self, n=1):
        for _ in range(max(0, int(n))):
            self._act("step", direction=1)

    def walk(self, steps=1):
        self.step(steps)

    def back(self, steps=1):
        for _ in range(max(0, int(steps))):
            self._act("step", direction=-1)

    def turn(self):
        self._act("turn")

    def jump(self, times=1):
        for _ in range(max(1, int(times))):
            self._act("jump")

    def spin(self):
        self._act("spin")

    def dance(self, beats=4):
        self._act("dance", beats=max(1, int(beats)))

    def wag(self):
        self._act("wag")

    def cheer(self):
        self._act("cheer")

    def sit(self):
        self._act("sit")

    def eat(self):
        self.__dict__["is_hungry"] = False
        self._act("eat")

    def sleep(self, seconds=2):
        self._act("sleep", seconds=float(seconds))

    def wake(self):
        self._act("wake")

    def birthday(self):
        self.__dict__["age"] = self.age + 1
        self._act("birthday", new_age=self.age)

    def grow(self, amount=0.2):
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            amount = 0.2
        self.__dict__["size"] = round(float(self.size) + amount, 3)
        self._act("grow", target=self.size)

    def shrink(self, amount=0.2):
        self.grow(-abs(float(amount)))

    def wait(self, seconds=1):
        self._act("wait", seconds=float(seconds))


# --------------------------------------------------------------------------
#  Helpers students can call
# --------------------------------------------------------------------------

def _caller_line():
    f = sys._getframe(1)
    uf = STAGE.user_file
    while f is not None:
        if uf and os.path.abspath(f.f_code.co_filename) == uf:
            return f.f_lineno
        f = f.f_back
    return None


def show(label, value):
    """Put any variable on the Variables panel so you can see its type."""
    STAGE.push({"kind": "show", "label": str(label), "value": value},
               line=_caller_line())


def ask(question="What do you think?"):
    """Pop up a question box and give back the answer as a string."""
    answer = STAGE.ask(str(question))
    return "" if answer is None else answer


def wait(seconds=1):
    STAGE.push({"kind": "wait", "seconds": float(seconds)}, line=_caller_line())


def help_me():
    lines = ["Things your pet can do:"]
    lines.append("  pet.say(...)      pet.think(...)   pet.step()     pet.walk(3)")
    lines.append("  pet.back(2)       pet.turn()       pet.jump()     pet.spin()")
    lines.append("  pet.dance()       pet.wag()        pet.cheer()    pet.sit()")
    lines.append("  pet.eat()         pet.sleep(2)     pet.wake()     pet.wait(1)")
    lines.append("  pet.birthday()    pet.grow(0.2)    pet.shrink(0.1)")
    lines.append("Things you can change:")
    lines.append("  pet.name   pet.age   pet.size   pet.color   pet.is_hungry   pet.mood")
    lines.append("Other helpers:  show('treats', 5)   ask('Your name?')   wait(1)")
    for ln in lines:
        print(ln)


# --------------------------------------------------------------------------
#  The stage (window, drawing, playback)
# --------------------------------------------------------------------------

class _Stage:
    def __init__(self):
        self.reset_all()
        self.root = None
        self.user_file = None
        self.user_main = None
        self.speed = 1.0
        self.collecting = False

    def reset_all(self):
        self.pets = []
        self.actions = []
        self.index = 0
        self.current = None
        self.frame = 0
        self.total = 0
        self.particles = []
        self.vars = {}
        self.var_order = []
        self.finished = False
        self.t = 0.0

    # ---------- collection ----------
    def register(self, pet):
        pet._v["tile"] = float(len(self.pets))
        pet._v["lane"] = len(self.pets) % 2
        self.pets.append(pet)
        self.push({"kind": "spawn", "pet": pet}, line=_caller_line())

    def push(self, action, line=None):
        if not self.collecting:
            return
        action["line"] = line
        self.actions.append(action)

    def ask(self, question):
        auto = os.environ.get("PETPAL_AUTO_ANSWER")
        if auto is not None:
            self.push({"kind": "print", "text": "%s  ->  %r" % (question, auto)},
                      line=_caller_line())
            return auto
        if self.root is None:
            return input(question + " ")
        ans = simpledialog.askstring("PetPal asks...", question, parent=self.root)
        self.push({"kind": "print", "text": "%s  ->  %r" % (question, ans)},
                  line=_caller_line())
        return ans

    # ---------- window ----------
    def build(self):
        self.root = tk.Tk()
        self.root.title("PetPal")
        self.root.configure(bg=BG)
        self.root.minsize(860, 580)

        fam = self._pick_font(["Comic Sans MS", "Chalkboard SE", "Verdana",
                               "Trebuchet MS", "DejaVu Sans"])
        mono = self._pick_font(["Menlo", "Consolas", "DejaVu Sans Mono",
                                "Courier New", "Courier"])
        self.F = lambda s, b=False: (fam, s, "bold" if b else "normal")
        self.M = lambda s, b=False: (mono, s, "bold" if b else "normal")

        top = tk.Frame(self.root, bg=BG)
        top.pack(fill="x", padx=14, pady=(12, 6))
        tk.Label(top, text="PetPal", font=self.F(22, True), bg=BG,
                 fg=ACCENT).pack(side="left")
        tk.Label(top, text="  your code, alive", font=self.F(10), bg=BG,
                 fg=SOFT).pack(side="left", pady=(8, 0))
        self.status = tk.Label(top, text="getting ready...", font=self.F(11, True),
                               bg=BG, fg=INK)
        self.status.pack(side="right", pady=(8, 0))

        body = tk.Frame(self.root, bg=BG)
        body.pack(fill="both", expand=True, padx=12, pady=(0, 10))

        # ---- left: the code
        left = self._card(body, "Your code")
        left.pack(side="left", fill="both", expand=False)
        self.code = tk.Text(left, width=33, height=10, font=self.M(9),
                            bg=PANEL, fg=INK, relief="flat", padx=10, pady=8,
                            wrap="none", highlightthickness=0, cursor="arrow")
        self.code.pack(fill="both", expand=True, padx=6, pady=(0, 8))
        self.code.tag_configure("now", background="#FFF0B8")
        self.code.tag_configure("num", foreground="#C9C2D3")
        self.code.configure(state="disabled")

        # ---- middle: the scene
        mid = tk.Frame(body, bg=BG)
        mid.pack(side="left", fill="both", expand=True, padx=10)
        self.canvas = tk.Canvas(mid, width=W, height=H, bg="#CFF0FF",
                                highlightthickness=3,
                                highlightbackground="#FFFFFF")
        self.canvas.pack()

        ctl = tk.Frame(mid, bg=BG)
        ctl.pack(pady=10)
        self._button(ctl, "Replay", self.replay, ACCENT).pack(side="left", padx=4)
        self._button(ctl, "Slower", lambda: self.set_speed(0.5), ACCENT2).pack(side="left", padx=4)
        self._button(ctl, "Normal", lambda: self.set_speed(1.0), ACCENT2).pack(side="left", padx=4)
        self._button(ctl, "Faster", lambda: self.set_speed(2.0), ACCENT2).pack(side="left", padx=4)
        self.speed_lbl = tk.Label(ctl, text="speed 1x", font=self.F(10), bg=BG, fg=SOFT)
        self.speed_lbl.pack(side="left", padx=10)

        # ---- right: variables + console
        right = tk.Frame(body, bg=BG)
        right.pack(side="left", fill="both", expand=False)

        vcard = self._card(right, "Variables")
        vcard.pack(fill="both", expand=True)
        self.varbox = tk.Frame(vcard, bg=PANEL)
        self.varbox.pack(fill="both", expand=True, padx=8, pady=(0, 8))

        ccard = self._card(right, "Console  -  print() lands here")
        ccard.pack(fill="both", expand=True, pady=(10, 0))
        self.console = tk.Text(ccard, width=27, height=9, font=self.M(9),
                               bg="#FDFAF5", fg=INK, relief="flat", padx=8,
                               pady=6, wrap="word", highlightthickness=0)
        self.console.pack(fill="both", expand=True, padx=6, pady=(0, 8))
        self.console.tag_configure("err", foreground="#C2405A")
        self.console.tag_configure("ok", foreground="#2E8B57")
        self.console.configure(state="disabled")

        self.load_code()

    def _card(self, parent, title):
        outer = tk.Frame(parent, bg=PANEL, highlightbackground=LINE,
                         highlightthickness=2)
        tk.Label(outer, text=title, font=self.F(10, True), bg=PANEL, fg=SOFT,
                 anchor="w").pack(fill="x", padx=12, pady=(8, 4))
        return outer

    def _button(self, parent, text, cmd, color):
        """A clickable label, not a tk.Button.

        macOS draws tk.Button with the native Aqua style and ignores 'bg',
        which left us with pale text on a pale native button. Labels honour
        their colours on every platform, so the buttons look the same - and
        stay readable - on macOS, Windows and Linux.
        """
        b = tk.Label(parent, text=text, font=self.F(10, True),
                     bg=color, fg=BTN_TEXT, padx=16, pady=6,
                     cursor="hand2", bd=0, highlightthickness=0)

        def press(_event):
            b.configure(bg=_shade(color, 0.86))
            b.after(90, lambda: b.configure(bg=_shade(color, 0.94)))
            cmd()

        b.bind("<Button-1>", press)
        b.bind("<Enter>", lambda e: b.configure(bg=_shade(color, 0.94)))
        b.bind("<Leave>", lambda e: b.configure(bg=color))
        return b

    def _pick_font(self, wanted):
        try:
            have = set(tkfont.families(self.root))
        except Exception:
            have = set()
        for w in wanted:
            if w in have:
                return w
        return wanted[-1]

    def _pick_font_pre(self, wanted):
        return wanted[0]

    def load_code(self):
        if not self.user_file or not os.path.exists(self.user_file):
            return
        try:
            with open(self.user_file, "r", encoding="utf-8") as fh:
                src = fh.read().splitlines()
        except OSError:
            return
        self.code.configure(state="normal")
        self.code.delete("1.0", "end")
        for i, ln in enumerate(src, 1):
            self.code.insert("end", "%3d " % i, "num")
            self.code.insert("end", ln + "\n")
        self.code.configure(state="disabled")
        self.src_len = len(src)

    def highlight(self, line):
        if line is None or not hasattr(self, "src_len"):
            return
        self.code.configure(state="normal")
        self.code.tag_remove("now", "1.0", "end")
        self.code.tag_add("now", "%d.0" % line, "%d.end+1c" % line)
        self.code.configure(state="disabled")
        self.code.see("%d.0" % max(1, line - 3))

    def log(self, text, tag=None):
        self.console.configure(state="normal")
        self.console.insert("end", text + "\n", tag or ())
        self.console.see("end")
        self.console.configure(state="disabled")

    def set_speed(self, s):
        self.speed = s
        self.speed_lbl.configure(text="speed %gx" % s)

    # ---------- variables panel ----------
    def set_var(self, label, value):
        if label not in self.vars:
            self.var_order.append(label)
        self.vars[label] = value
        self.render_vars()

    def render_vars(self):
        for child in self.varbox.winfo_children():
            child.destroy()
        for label in self.var_order:
            value = self.vars[label]
            tname = type(value).__name__
            bgc, fgc = TYPE_COLORS.get(tname, ("#EEEAF5", "#5A5368"))
            row = tk.Frame(self.varbox, bg=PANEL)
            row.pack(fill="x", pady=2)
            tk.Label(row, text=label, font=self.M(10, True), bg=PANEL, fg=INK,
                     width=10, anchor="w").pack(side="left")
            tk.Label(row, text=tname, font=self.F(8, True), bg=bgc, fg=fgc,
                     padx=6, pady=1).pack(side="left", padx=(0, 6))
            shown = repr(value) if isinstance(value, str) else str(value)
            if len(shown) > 13:
                shown = shown[:12] + "..."
            tk.Label(row, text=shown, font=self.M(10), bg=PANEL, fg=fgc,
                     anchor="w").pack(side="left")

    # ---------- running ----------
    def start(self):
        self.root.after(500, self._collect_and_play)
        self.root.after(FPS_MS, self._tick)
        self.root.mainloop()

    def replay(self):
        self.reset_all()
        self.render_vars()
        self.console.configure(state="normal")
        self.console.delete("1.0", "end")
        self.console.configure(state="disabled")
        self.root.after(200, self._collect_and_play)

    def _collect_and_play(self):
        self.collecting = True
        self.status.configure(text="reading your code...")
        real_stdout = sys.stdout
        sys.stdout = _Tee(real_stdout, self)
        try:
            self.user_main()
        except Exception as exc:  # noqa: BLE001 - we want every mistake
            sys.stdout = real_stdout
            self.actions.append({"kind": "error", "exc": exc,
                                 "line": _error_line(exc, self.user_file)})
        finally:
            sys.stdout = real_stdout
        self.collecting = False
        self.index = 0
        self.finished = False
        self._next()

    def _next(self):
        if self.index >= len(self.actions):
            self.current = None
            self.finished = True
            self.status.configure(text="Program finished!  Press Replay to watch again.")
            self.code.configure(state="normal")
            self.code.tag_remove("now", "1.0", "end")
            self.code.configure(state="disabled")
            return
        a = self.actions[self.index]
        self.index += 1
        self.current = a
        self.frame = 0
        self.highlight(a.get("line"))
        self.total = max(1, int(self._begin(a) / max(0.2, self.speed)))

    # ---------- action handling ----------
    def _begin(self, a):
        k = a["kind"]
        pet = a.get("pet")
        v = pet._v if pet is not None else None

        if k == "spawn":
            v.update({"name": pet.name, "age": pet.age, "color": pet.color,
                      "size": float(pet.size)})
            self.status.configure(text="A %s appears!" % pet.kind)
            self._burst(self._pet_x(pet), GROUND - 60, "#FFD966", 14)
            return 14

        if k == "set":
            key, val = a["key"], a["value"]
            self.set_var(key, val)
            if key == "name":
                v["name"] = str(val)
                self.status.configure(text='name is now "%s"' % val)
                self._burst(self._pet_x(pet), GROUND - 110, ACCENT, 10)
            elif key == "age":
                v["age"] = val
                self.status.configure(text="age is now %s" % val)
            elif key == "color":
                v["color"] = val
                self._burst(self._pet_x(pet), GROUND - 70, _resolve_color(val), 12)
            elif key == "size":
                a["from"] = v["size"]
                a["to"] = _clamp(float(val), 0.35, 2.1)
                self.status.configure(text="size is now %s" % val)
                return 22
            elif key == "is_hungry":
                v["hungry"] = bool(val)
                v["mouth"] = "sad" if val else "smile"
            elif key == "mood":
                v["mood"] = str(val)
                self._apply_mood(v, str(val))
            else:
                self.status.configure(text="%s = %r" % (key, val))
            return 10

        if k == "show":
            self.set_var(a["label"], a["value"])
            self.status.configure(text="%s is a %s" % (a["label"],
                                                       type(a["value"]).__name__))
            return 10

        if k == "print":
            self.log(a["text"])
            return 6

        if k == "say":
            v["bubble"] = a["text"]
            v["bubble_kind"] = a.get("bubble", "say")
            v["mouth"] = "open"
            self.status.configure(text="%s says something" % v["name"])
            return max(30, min(120, 18 + len(a["text"]) * 1.6))

        if k == "step":
            a["from"] = v["tile"]
            d = a["direction"] * (1 if v["facing"] > 0 else -1)
            a["to"] = _clamp(v["tile"] + d, 0, NTILES - 1)
            if a["to"] == a["from"]:
                self.status.configure(text="bumped into the fence!")
            else:
                self.status.configure(text="step!")
            return 24

        if k == "turn":
            self.status.configure(text="turning around")
            return 14

        if k == "jump":
            self.status.configure(text="boing!")
            self._burst(self._pet_x(pet), GROUND - 20, "#FFFFFF", 8)
            return 26

        if k == "spin":
            self.status.configure(text="spinning!")
            return 30

        if k == "dance":
            self.status.configure(text="dancing!")
            return 22 * a["beats"]

        if k == "wag":
            self.status.configure(text="happy wiggles")
            return 26

        if k == "cheer":
            self.status.configure(text="hooray!")
            self._burst(self._pet_x(pet), GROUND - 130, ACCENT, 22, star=True)
            return 26

        if k == "sit":
            self.status.configure(text="good pet!")
            return 20

        if k == "eat":
            v["hungry"] = False
            self.set_var("is_hungry", False)
            self.status.configure(text="nom nom nom")
            return 46

        if k == "sleep":
            v["asleep"] = True
            v["eyes"] = "closed"
            self.status.configure(text="zzz...")
            return max(20, int(a["seconds"] * 30))

        if k == "wake":
            v["asleep"] = False
            v["eyes"] = "open"
            self.status.configure(text="good morning!")
            return 14

        if k == "birthday":
            v["age"] = a["new_age"]
            self.set_var("age", a["new_age"])
            self.status.configure(text="Happy birthday! Now %s years old"
                                       % a["new_age"])
            self._burst(self._pet_x(pet), GROUND - 140, "#FFD166", 26, star=True)
            return 52

        if k == "grow":
            a["from"] = v["size"]
            a["to"] = _clamp(float(a["target"]), 0.35, 2.1)
            self.set_var("size", round(float(a["target"]), 3))
            self.status.configure(text="size -> %.2f" % a["target"])
            return 26

        if k == "wait":
            self.status.configure(text="waiting...")
            return max(6, int(a["seconds"] * 30))

        if k == "error":
            self.log("Oops! Something went wrong", "err")
            if a.get("line"):
                self.log("  on line %d of your file" % a["line"], "err")
            self.log(_friendly(a["exc"]), "err")
            self.status.configure(text="There is a bug to fix - see the Console")
            return 20

        return 8

    def _update(self, a, t):
        k = a["kind"]
        pet = a.get("pet")
        v = pet._v if pet is not None else None

        if k == "step":
            v["tile"] = a["from"] + (a["to"] - a["from"]) * _ease(t)
            v["legs"] = math.sin(t * math.pi * 4) * 1.0
            v["bob"] = abs(math.sin(t * math.pi * 4)) * 5
        elif k == "set" and a["key"] == "size":
            v["size"] = a["from"] + (a["to"] - a["from"]) * _ease(t)
        elif k == "grow":
            v["size"] = a["from"] + (a["to"] - a["from"]) * _ease(t)
            v["squash"] = 1 + math.sin(t * math.pi) * 0.12
        elif k == "turn":
            v["squash"] = 1 - math.sin(t * math.pi) * 0.45
            if t > 0.5 and not a.get("done"):
                a["done"] = True
                v["facing"] *= -1
        elif k == "jump":
            v["y_off"] = -math.sin(t * math.pi) * 74
            v["squash"] = 1 + math.sin(t * math.pi) * 0.1
            v["legs"] = 1.4
        elif k == "spin":
            v["spin"] = t
            v["squash"] = abs(math.cos(t * math.pi * 2)) * 0.9 + 0.1
            v["y_off"] = -math.sin(t * math.pi) * 24
        elif k == "dance":
            v["y_off"] = -abs(math.sin(t * math.pi * a["beats"] * 2)) * 26
            v["lean"] = math.sin(t * math.pi * a["beats"] * 2) * 0.35
            v["tail"] = math.sin(t * 40) * 1.4
            if random.random() < 0.12:
                self._burst(self._pet_x(pet), GROUND - 120,
                            random.choice(["#FFD166", ACCENT, ACCENT2, "#A6E5CB"]), 3)
        elif k == "wag":
            v["tail"] = math.sin(t * 34) * 1.6
            v["y_off"] = -abs(math.sin(t * math.pi * 3)) * 8
        elif k == "cheer":
            v["y_off"] = -abs(math.sin(t * math.pi * 2)) * 50
            v["eyes"] = "happy"
        elif k == "sit":
            v["y_off"] = math.sin(t * math.pi) * 10
        elif k == "eat":
            v["bowl"] = min(1.0, t * 3)
            v["y_off"] = math.sin(t * math.pi * 6) * 6
            v["mouth"] = "open" if int(t * 12) % 2 else "smile"
            if random.random() < 0.1:
                self._burst(self._pet_x(pet), GROUND - 100, ACCENT, 3, heart=True)
        elif k == "sleep":
            v["y_off"] = math.sin(t * math.pi * 2) * 3
            if random.random() < 0.05:
                self.particles.append({"x": self._pet_x(pet) + 34,
                                       "y": GROUND - 120, "vx": 0.5, "vy": -0.9,
                                       "life": 40, "color": "#9AA7C7", "kind": "z"})
        elif k == "birthday":
            v["y_off"] = -abs(math.sin(t * math.pi * 3)) * 34
            v["cake"] = 1.0 if t < 0.75 else max(0.0, (1 - t) * 4)
            v["eyes"] = "happy"
        elif k == "say":
            v["mouth"] = "open" if int(t * 14) % 2 else "smile"

    def _end(self, a):
        pet = a.get("pet")
        if pet is not None:
            v = pet._v
            v["y_off"] = 0.0
            v["squash"] = 1.0
            v["lean"] = 0.0
            v["legs"] = 0.0
            v["spin"] = 0.0
            v["bowl"] = 0.0
            v["cake"] = 0.0
            if a["kind"] in ("say",):
                v["bubble"] = None
            if a["kind"] in ("cheer", "birthday") and not v["asleep"]:
                v["eyes"] = "open"
            if a["kind"] == "sleep":
                v["eyes"] = "closed"
            if a["kind"] == "eat":
                v["mouth"] = "smile"

    def _apply_mood(self, v, mood):
        m = mood.lower()
        if m in ("sad", "grumpy"):
            v["mouth"], v["eyes"] = "sad", "open"
        elif m in ("sleepy", "tired"):
            v["mouth"], v["eyes"] = "smile", "sleepy"
        elif m in ("excited", "happy", "silly"):
            v["mouth"], v["eyes"] = "smile", "happy"
        elif m in ("surprised", "shocked"):
            v["mouth"], v["eyes"] = "open", "wide"
        else:
            v["mouth"], v["eyes"] = "smile", "open"

    # ---------- main loop ----------
    def _tick(self):
        self.t += 1
        if self.current is not None:
            self.frame += 1
            t = min(1.0, self.frame / float(self.total))
            self._update(self.current, t)
            if self.frame >= self.total:
                self._end(self.current)
                self._next()
        for p in self.pets:
            self._idle(p)
        self._update_particles()
        self._draw()
        self.root.after(FPS_MS, self._tick)

    def _idle(self, pet):
        v = pet._v
        if self.current is None or self.current.get("pet") is not pet:
            v["y_off"] *= 0.8
            v["legs"] *= 0.8
            v["lean"] *= 0.85
            v["squash"] += (1 - v["squash"]) * 0.2
        v["bob"] = math.sin(self.t * 0.09) * 2.4
        if not v["asleep"]:
            v["tail"] = v["tail"] * 0.85 + math.sin(self.t * 0.16) * 0.45
            v["blink"] -= 1
            if v["blink"] < -60 and random.random() < 0.03:
                v["blink"] = 6
        else:
            v["tail"] *= 0.9

    def _update_particles(self):
        for p in self.particles:
            p["x"] += p["vx"]
            p["y"] += p["vy"]
            p["vy"] += 0.06 if p["kind"] != "z" else -0.01
            p["life"] -= 1
        self.particles = [p for p in self.particles if p["life"] > 0]

    def _burst(self, x, y, color, n, star=False, heart=False):
        kind = "star" if star else ("heart" if heart else "dot")
        for _ in range(n):
            self.particles.append({
                "x": x + random.uniform(-22, 22), "y": y + random.uniform(-14, 14),
                "vx": random.uniform(-2.2, 2.2), "vy": random.uniform(-3.4, -0.6),
                "life": random.randint(22, 44), "color": color, "kind": kind})

    # ---------- drawing ----------
    def _pet_x(self, pet):
        return TILE0 + pet._v["tile"] * TILEW

    def _draw(self):
        c = self.canvas
        c.delete("all")
        self._draw_scene()
        for pet in sorted(self.pets, key=lambda p: (p._v["lane"], p._v["tile"])):
            self._draw_pet(pet)
        self._draw_particles()
        for pet in self.pets:
            if pet._v["bubble"]:
                self._draw_bubble(pet)

    def _draw_scene(self):
        c = self.canvas
        c.create_rectangle(0, 0, W, GROUND - 4, fill="#CFF0FF", outline="")
        c.create_oval(W - 110, -34, W - 10, 66, fill="#FFE58A", outline="")
        c.create_oval(W - 96, -20, W - 24, 52, fill="#FFEFAE", outline="")
        for cx, cy, s in ((90, 54, 1.0), (250, 34, 0.7), (420, 70, 0.85)):
            self._cloud(cx, cy, s)
        # hills
        c.create_oval(-70, GROUND - 130, 210, GROUND + 80, fill="#B9E7A8", outline="")
        c.create_oval(300, GROUND - 110, 620, GROUND + 80, fill="#B9E7A8", outline="")
        # ground
        c.create_rectangle(0, GROUND - 4, W, H, fill="#93D97F", outline="")
        c.create_rectangle(0, GROUND - 4, W, GROUND + 6, fill="#A8E491", outline="")
        # fence at the end
        fx = TILE0 + (NTILES - 0.35) * TILEW
        c.create_rectangle(fx, GROUND - 76, fx + 10, GROUND + 6, fill="#E8C9A0",
                           outline="#C9A377")
        c.create_rectangle(fx + 26, GROUND - 76, fx + 36, GROUND + 6, fill="#E8C9A0",
                           outline="#C9A377")
        c.create_rectangle(fx - 6, GROUND - 60, fx + 44, GROUND - 50, fill="#E8C9A0",
                           outline="#C9A377")
        # stepping stones with numbers
        for i in range(NTILES):
            x = TILE0 + i * TILEW
            c.create_oval(x - 24, GROUND + 4, x + 24, GROUND + 24,
                          fill="#86CE73", outline="#79C066")
            c.create_text(x, GROUND + 14, text=str(i), fill="#FFFFFF",
                          font=self.F(9, True))
        # flowers
        random.seed(7)
        for _ in range(9):
            x = random.randint(12, W - 12)
            y = random.randint(GROUND + 34, H - 12)
            col = random.choice(["#FF9EB8", "#FFD166", "#C3A7F0", "#FFFFFF"])
            for a in range(5):
                ang = a * 72 * math.pi / 180
                c.create_oval(x + math.cos(ang) * 5 - 3.5, y + math.sin(ang) * 5 - 3.5,
                              x + math.cos(ang) * 5 + 3.5, y + math.sin(ang) * 5 + 3.5,
                              fill=col, outline="")
            c.create_oval(x - 2.2, y - 2.2, x + 2.2, y + 2.2, fill="#FFE066", outline="")
        random.seed()

    def _cloud(self, x, y, s):
        c = self.canvas
        for dx, dy, r in ((0, 0, 26), (22, 6, 20), (-22, 6, 18), (8, -10, 18)):
            c.create_oval(x + (dx - r) * s, y + (dy - r) * s,
                          x + (dx + r) * s, y + (dy + r) * s,
                          fill="#FFFFFF", outline="")

    def _draw_pet(self, pet):
        c = self.canvas
        v = pet._v
        s = _clamp(v["size"], 0.35, 2.1) * 0.85
        x = self._pet_x(pet) + v["lane"] * 20
        base = GROUND + 6 + v["lane"] * 40
        body_col = _resolve_color(v["color"])
        dark = _shade(body_col, 0.86)
        light = _shade(body_col, 1.14)
        face = v["facing"]
        sq = v["squash"]
        lean = v["lean"]

        # shadow
        c.create_oval(x - 40 * s, base - 8, x + 40 * s, base + 8,
                      fill="#6FBF5C", outline="")

        yb = base + v["y_off"] + v["bob"]          # feet line
        hgt = 132 * s * sq
        # ---- legs
        legsw = 13 * s
        for i, dx in enumerate((-19 * s, 19 * s)):
            off = v["legs"] * (8 * s) * (1 if i == 0 else -1)
            c.create_oval(x + dx - legsw + off, yb - 30 * s,
                          x + dx + legsw + off, yb, fill=dark, outline="")
        # ---- tail
        self._draw_tail(pet, x, yb, s, body_col, dark)
        # ---- body
        bw, bh = 40 * s, 44 * s
        cy = yb - 40 * s
        c.create_oval(x - bw, cy - bh, x + bw, cy + bh, fill=body_col, outline="")
        c.create_oval(x - bw * 0.58, cy - bh * 0.45, x + bw * 0.58, cy + bh * 0.82,
                      fill=light, outline="")
        # ---- front paws
        for dx in (-24 * s, 24 * s):
            c.create_oval(x + dx - 11 * s, cy + bh - 16 * s,
                          x + dx + 11 * s, cy + bh + 6 * s, fill=body_col, outline="")

        # ---- head
        hr = 42 * s
        hx = x + lean * 16 * s
        hy = yb - hgt + hr * 0.55
        if pet.kind == "cat":
            for sgn in (-1, 1):
                c.create_polygon(hx + sgn * 17 * s, hy - hr * 0.72,
                                 hx + sgn * 40 * s, hy - hr * 1.42,
                                 hx + sgn * 41 * s, hy - hr * 0.42,
                                 fill=body_col, outline="", smooth=False)
                c.create_polygon(hx + sgn * 22 * s, hy - hr * 0.76,
                                 hx + sgn * 35 * s, hy - hr * 1.18,
                                 hx + sgn * 35 * s, hy - hr * 0.56,
                                 fill="#FFC7D4", outline="")
        else:
            for sgn in (-1, 1):
                c.create_oval(hx + sgn * 30 * s - 15 * s, hy - hr * 0.62,
                              hx + sgn * 30 * s + 15 * s, hy + hr * 0.66,
                              fill=dark, outline="")
        c.create_oval(hx - hr, hy - hr, hx + hr, hy + hr, fill=body_col, outline="")

        # muzzle
        mw, mh = 24 * s, 17 * s
        my = hy + hr * 0.34
        hx = hx + face * 5 * s
        c.create_oval(hx - mw, my - mh, hx + mw, my + mh, fill=_shade(body_col, 1.22),
                      outline="")
        # cheeks
        for sgn in (-1, 1):
            c.create_oval(hx + sgn * 30 * s - 9 * s, hy + 8 * s,
                          hx + sgn * 30 * s + 9 * s, hy + 20 * s,
                          fill="#FFB6C9", outline="")
        # eyes
        ex = 17 * s
        ey = hy - 7 * s
        blinking = v["blink"] > 0
        eyes = v["eyes"]
        for sgn in (-1, 1):
            px = hx + sgn * ex
            if blinking or eyes == "closed":
                c.create_line(px - 8 * s, ey, px + 8 * s, ey, width=3 * s,
                              fill="#4A4458", capstyle="round")
            elif eyes == "happy":
                c.create_arc(px - 9 * s, ey - 9 * s, px + 9 * s, ey + 9 * s,
                             start=20, extent=140, style="arc", width=3 * s,
                             outline="#4A4458")
            elif eyes == "sleepy":
                c.create_arc(px - 9 * s, ey - 4 * s, px + 9 * s, ey + 12 * s,
                             start=0, extent=-180, style="arc", width=3 * s,
                             outline="#4A4458")
            else:
                rr = 11 * s if eyes == "wide" else 9 * s
                c.create_oval(px - rr, ey - rr * 1.12, px + rr, ey + rr * 1.12,
                              fill="#4A4458", outline="")
                c.create_oval(px - rr * 0.2, ey - rr * 0.86,
                              px + rr * 0.52, ey - rr * 0.16,
                              fill="#FFFFFF", outline="")
        # nose + mouth
        c.create_oval(hx - 6 * s, my - 9 * s, hx + 6 * s, my - 1 * s,
                      fill="#6A5A66" if pet.kind == "dog" else "#F58FA8", outline="")
        mouth = v["mouth"]
        if mouth == "open":
            c.create_oval(hx - 8 * s, my + 1 * s, hx + 8 * s, my + 13 * s,
                          fill="#C2607A", outline="")
        elif mouth == "sad":
            c.create_arc(hx - 11 * s, my + 6 * s, hx + 11 * s, my + 20 * s,
                         start=0, extent=180, style="arc", width=2.4 * s,
                         outline="#6A5A66")
        else:
            for sgn in (-1, 1):
                c.create_arc(hx + sgn * 6 * s - 6 * s, my - 2 * s,
                             hx + sgn * 6 * s + 6 * s, my + 10 * s,
                             start=200, extent=140, style="arc", width=2.2 * s,
                             outline="#6A5A66")
        if pet.kind == "cat":
            for sgn in (-1, 1):
                for k in (-1, 0, 1):
                    c.create_line(hx + sgn * 14 * s, my + k * 4 * s - 2 * s,
                                  hx + sgn * 40 * s, my + k * 7 * s - 6 * s,
                                  fill="#FFFFFF", width=1.6 * s)

        # collar + name tag
        ny = yb - hgt + hr * 1.62
        c.create_rectangle(x - 26 * s, ny - 5 * s, x + 26 * s, ny + 5 * s,
                           fill=ACCENT, outline="")
        c.create_oval(x - 8 * s, ny + 2 * s, x + 8 * s, ny + 18 * s,
                      fill="#FFD166", outline="#E8B94A")
        initial = (str(v["name"])[:1] or "?").upper()
        c.create_text(x, ny + 10 * s, text=initial, font=self.F(int(9 * s) + 5, True),
                      fill="#8A6A18")

        # name + age badge floating above
        label = "%s   %s" % (v["name"], _age_text(v["age"]))
        top = hy - hr * (1.52 if pet.kind == "cat" else 1.02)
        ty = max(20, top - 20 * s)
        tw = 7.2 * len(label) + 26
        tcx = _clamp(x, tw / 2 + 6, W - tw / 2 - 6)
        self._rounded(tcx - tw / 2, ty - 14, tcx + tw / 2, ty + 14, 13, "#FFFFFF",
                      "#F0DFE8")
        c.create_text(tcx, ty, text=label, font=self.F(11, True), fill=INK)
        v["badge_y"] = ty

        # food bowl
        if v["bowl"] > 0.02:
            bx = x + face * 44 * s
            c.create_arc(bx - 24, GROUND - 16, bx + 24, GROUND + 14, start=180,
                         extent=180, fill="#7FC8F8", outline="#5FAEE0")
            c.create_oval(bx - 16, GROUND - 18, bx + 16, GROUND - 6,
                          fill="#D98A5A", outline="")
        # cake
        if v["cake"] > 0.02:
            cx2 = x + 62 * s
            c.create_rectangle(cx2 - 22, GROUND - 46, cx2 + 22, GROUND - 12,
                               fill="#FFD9E6", outline="#F0B9CE")
            c.create_rectangle(cx2 - 22, GROUND - 34, cx2 + 22, GROUND - 26,
                               fill="#FFFFFF", outline="")
            c.create_rectangle(cx2 - 2, GROUND - 62, cx2 + 2, GROUND - 46,
                               fill="#9BD3F5", outline="")
            c.create_oval(cx2 - 4, GROUND - 72, cx2 + 4, GROUND - 60,
                          fill="#FFD166", outline="")

    def _draw_tail(self, pet, x, yb, s, body_col, dark):
        c = self.canvas
        v = pet._v
        wag = v["tail"]
        tx = x - v["facing"] * 34 * s
        ty = yb - 44 * s
        if pet.kind == "cat":
            pts = []
            for i in range(7):
                f = i / 6.0
                px = tx - v["facing"] * (f * 34 * s) + math.sin(f * 3 + wag) * 12 * s
                py = ty - f * 56 * s
                pts.extend([px, py])
            c.create_line(*pts, smooth=True, width=11 * s, fill=body_col,
                          capstyle="round")
            c.create_oval(pts[-2] - 6 * s, pts[-1] - 6 * s,
                          pts[-2] + 6 * s, pts[-1] + 6 * s,
                          fill=_shade(body_col, 1.2), outline="")
        else:
            f = v["facing"]
            ang = -0.55 + wag * 0.38
            px = tx - f * math.cos(ang) * 34 * s
            py = ty + math.sin(ang) * 34 * s
            c.create_line(tx + f * 8 * s, ty + 8 * s,
                          (tx + px) / 2 - f * 12 * s, (ty + py) / 2 - 4 * s,
                          px, py, smooth=True, width=12 * s, fill=dark,
                          capstyle="round")
            c.create_oval(px - 7 * s, py - 7 * s, px + 7 * s, py + 7 * s,
                          fill=_shade(body_col, 1.08), outline="")

    def _rounded(self, x0, y0, x1, y1, r, fill, outline):
        c = self.canvas
        c.create_oval(x0, y0, x0 + 2 * r, y0 + 2 * r, fill=fill, outline=outline)
        c.create_oval(x1 - 2 * r, y0, x1, y0 + 2 * r, fill=fill, outline=outline)
        c.create_oval(x0, y1 - 2 * r, x0 + 2 * r, y1, fill=fill, outline=outline)
        c.create_oval(x1 - 2 * r, y1 - 2 * r, x1, y1, fill=fill, outline=outline)
        c.create_rectangle(x0 + r, y0, x1 - r, y1, fill=fill, outline=fill)
        c.create_rectangle(x0, y0 + r, x1, y1 - r, fill=fill, outline=fill)

    def _draw_bubble(self, pet):
        c = self.canvas
        v = pet._v
        s = _clamp(v["size"], 0.35, 2.1) * 0.85
        text = str(v["bubble"])
        lines = _wrap(text, 22)
        wpx = max(60, min(260, max(len(l) for l in lines) * 8 + 30))
        hpx = len(lines) * 19 + 18
        x = self._pet_x(pet) + 30 * s
        y = v.get("badge_y", 60) - 20 - hpx
        x = _clamp(x, 8, W - wpx - 8)
        if y < 6:
            y = 6
            x = _clamp(self._pet_x(pet) + 70 * s, 8, W - wpx - 8)
        self._rounded(x, y, x + wpx, y + hpx, 14, "#FFFFFF", "#E6DCEB")
        if v["bubble_kind"] == "think":
            for i, r in enumerate((7, 5, 3)):
                c.create_oval(x + 12 - r + i * 6, y + hpx + 4 + i * 9 - r,
                              x + 12 + r + i * 6, y + hpx + 4 + i * 9 + r,
                              fill="#FFFFFF", outline="#E6DCEB")
        else:
            c.create_polygon(x + 14, y + hpx - 2, x + 40, y + hpx - 2,
                             x + 10, y + hpx + 20, fill="#FFFFFF", outline="")
        c.create_text(x + wpx / 2, y + hpx / 2, text="\n".join(lines),
                      font=self.F(11), fill=INK, justify="center")

    def _draw_particles(self):
        c = self.canvas
        for p in self.particles:
            x, y = p["x"], p["y"]
            if p["kind"] == "star":
                pts = []
                for i in range(10):
                    r = 7 if i % 2 == 0 else 3
                    a = i * 36 * math.pi / 180 - math.pi / 2
                    pts.extend([x + math.cos(a) * r, y + math.sin(a) * r])
                c.create_polygon(pts, fill=p["color"], outline="")
            elif p["kind"] == "heart":
                c.create_oval(x - 6, y - 5, x, y + 1, fill=p["color"], outline="")
                c.create_oval(x, y - 5, x + 6, y + 1, fill=p["color"], outline="")
                c.create_polygon(x - 6, y - 1, x + 6, y - 1, x, y + 8,
                                 fill=p["color"], outline="")
            elif p["kind"] == "z":
                c.create_text(x, y, text="z", font=self.F(13, True), fill=p["color"])
            else:
                c.create_oval(x - 4, y - 4, x + 4, y + 4, fill=p["color"], outline="")


class _Tee:
    """Sends print() to the real terminal AND to the on-screen console."""

    def __init__(self, real, stage):
        self.real = real
        self.stage = stage
        self.buf = ""

    def write(self, text):
        self.real.write(text)
        self.buf += text
        while "\n" in self.buf:
            line, self.buf = self.buf.split("\n", 1)
            self.stage.push({"kind": "print", "text": line}, line=_caller_line())

    def flush(self):
        self.real.flush()


def _error_line(exc, user_file):
    tb = exc.__traceback__
    line = None
    while tb is not None:
        if user_file and os.path.abspath(tb.tb_frame.f_code.co_filename) == user_file:
            line = tb.tb_lineno
        tb = tb.tb_next
    return line


def _clamp(v, lo, hi):
    return max(lo, min(hi, v))


def _ease(t):
    return t * t * (3 - 2 * t)


def _age_text(age):
    try:
        n = float(age)
    except (TypeError, ValueError):
        return str(age)
    if n == 1:
        return "1 year old"
    if n == int(n):
        n = int(n)
    return "%s years old" % n


def _wrap(text, width):
    words, lines, cur = str(text).split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width and cur:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return lines or [""]


STAGE = _Stage()


def run(main_function):
    """Start PetPal and run your main() function. Put this at the bottom."""
    if not callable(main_function):
        print("run() needs your main function, like this:   run(main)")
        return
    STAGE.user_main = main_function
    try:
        STAGE.user_file = os.path.abspath(main_function.__code__.co_filename)
    except AttributeError:
        STAGE.user_file = None
    STAGE.build()
    STAGE.start()


__all__ = ["Pet", "run", "show", "ask", "wait", "help_me", "COLORS"]
