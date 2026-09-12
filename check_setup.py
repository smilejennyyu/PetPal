# =========================================================
#   CHECK MY SETUP
#
#   Run this any time you are not sure whether your computer
#   is ready. It never changes anything - it just looks.
#
#       python check_setup.py
# =========================================================

import os
import subprocess
import sys

OK = "  [ OK ]  "
NO = "  [ !! ]  "

print()
print("=" * 54)
print("  PetPal setup check")
print("=" * 54)
print()

# ---------- 1. Python itself ----------
v = sys.version_info
print("  Python version:  %d.%d.%d" % (v.major, v.minor, v.micro))
if v >= (3, 8):
    print(OK + "Python is new enough.")
else:
    print(NO + "PetPal needs Python 3.8 or newer.")
print("  Python lives at: " + sys.executable)
print()

# ---------- 2. tkinter (the window) ----------
try:
    import tkinter
    print(OK + "tkinter found (version %s) - PetPal can draw its window." % tkinter.TkVersion)
except ImportError:
    print(NO + "tkinter is MISSING. PetPal cannot open a window.")
    print("          Mac/Windows: reinstall Python from python.org.")
    print("          Linux:       sudo apt install python3-tk")
print()

# ---------- 3. petpal itself ----------
here = os.path.dirname(os.path.abspath(__file__))
if os.path.exists(os.path.join(here, "petpal.py")):
    print(OK + "petpal.py is in this folder.")
else:
    print(NO + "petpal.py is NOT in this folder.")
    print("          Run this file from inside the PetPal folder.")
print()

# ---------- 4. Sessions 1-4 verdict ----------
print("-" * 54)
print("  Everything above is all you need for Sessions 1-4.")
print("  You do NOT need Anaconda, pip, or a virtual")
print("  environment to play with your pet.")
print("-" * 54)
print()

# ---------- 5. Session 5 extras ----------
print("  Session 5 extras (ignore these until Session 5):")
print()

env = os.environ.get("CONDA_DEFAULT_ENV")
if env:
    print(OK + "conda environment active: %s" % env)
    if env == "base":
        print("          (that's the 'base' one - for Session 5 you want 'petpal')")
else:
    print("  [ -- ]  No conda environment active. That's fine for now.")

try:
    import matplotlib
    print(OK + "matplotlib %s is installed." % matplotlib.__version__)
except ImportError:
    print("  [ -- ]  matplotlib is not installed yet. You'll install it in Session 5.")

try:
    out = subprocess.run(["git", "--version"], capture_output=True, text=True, timeout=10)
    if out.returncode == 0:
        print(OK + out.stdout.strip())
    else:
        print("  [ -- ]  git is not installed yet. You'll install it in Session 5.")
except (OSError, subprocess.SubprocessError):
    print("  [ -- ]  git is not installed yet. You'll install it in Session 5.")

print()
print("=" * 54)
print()
