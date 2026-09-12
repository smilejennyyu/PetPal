# =========================================================
#   SESSION 5  -  YOUR PET'S GROWTH CHART
#
#   This is the first program in the course that needs
#   something Python does NOT come with: matplotlib.
#
#   Run it BEFORE you install anything. It will crash, and
#   the crash is the whole point of today's lesson.
#
#   Then install it:
#       conda activate petpal
#       conda install matplotlib
#
#   ...and run it again.
# =========================================================

import matplotlib.pyplot as plt


def main():
    # ---- the same growth rule you wrote in Session 3 ----
    # but this time we write the numbers down as we go.
    name = "Mochi"
    age = 0
    size = 0.5

    ages = []
    sizes = []

    for year in range(12):
        age = age + 1
        if age <= 3:
            size = size + 0.3      # growing fast
        elif age <= 6:
            size = size + 0.05     # slowing down
        else:
            size = size            # all grown up

        ages.append(age)
        sizes.append(round(size, 2))

    print("ages: ", ages)
    print("sizes:", sizes)

    # ---- now the new part: draw it ----------------------
    plt.figure(figsize=(7, 4.5))
    plt.plot(ages, sizes, marker="o", linewidth=2.5,
             color="#E85C8C", markerfacecolor="#FFFFFF")

    plt.title(f"{name}'s growth chart")
    plt.xlabel("age (years)")
    plt.ylabel("size")
    plt.grid(True, alpha=0.3)
    plt.ylim(0, max(sizes) + 0.4)

    # mark the moment the growing stops
    plt.axvline(x=3, linestyle="--", color="#7FC8F8")
    plt.text(3.15, 0.2, "growth slows here", color="#3E96D8")

    plt.tight_layout()
    plt.savefig("growth_chart.png", dpi=150)
    print("Saved growth_chart.png - open it!")
    plt.show()


main()


# =========================================================
#   YOUR TURN
#
#   1. Change the growth rule and re-run. Watch the shape
#      of the line change.
#   2. Plot TWO pets on the same chart - one that grows fast
#      and one that grows slowly. Add plt.legend().
#      Hint: call plt.plot() twice, with label="Mochi".
#   3. Change the colours. Find a hex code you like.
#
#   This is genuinely what a scientist's plotting code looks
#   like. Lists, a loop, an if statement, and matplotlib.
# =========================================================
