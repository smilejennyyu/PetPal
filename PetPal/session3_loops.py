# =========================================================
#   SESSION 3  -  LOOPS (make the computer do the boring bits)
#   Today: for loops, range(), counters, while loops,
#          and loops inside loops
# =========================================================

from petpal import *


def main():

    pet = Pet("dog")
    pet.name = "Pixel"
    pet.color = "peach"
    pet.age = 1
    pet.size = 0.7

    # -----------------------------------------------------
    # 1. THE LAZY WAY IS THE SMART WAY
    #    Instead of writing pet.step() five times...
    #    ...ask Python to repeat it for you.
    #
    #    range(5) means: 0, 1, 2, 3, 4   (five numbers)
    # -----------------------------------------------------
    pet.say("Watch me take 4 steps with a loop!")

    for i in range(4):
        pet.step()

    # -----------------------------------------------------
    # 2. THE LOOP VARIABLE
    #    i changes every time round the loop. You can use it!
    # -----------------------------------------------------
    pet.turn()
    for i in range(4):
        pet.say(f"step number {i}")
        pet.step()
    pet.turn()

    # -----------------------------------------------------
    # 3. range() HAS SUPERPOWERS
    #      range(5)        ->  0 1 2 3 4
    #      range(1, 6)     ->  1 2 3 4 5
    #      range(0, 10, 2) ->  0 2 4 6 8   (count by 2s)
    # -----------------------------------------------------
    for year in range(1, 4):
        print("Year", year)

    # -----------------------------------------------------
    # 4. A LOOP WITH AN IF INSIDE  -  the growth simulator
    #    Every birthday the pet grows... but only until 3.
    # -----------------------------------------------------
    for year in range(1, 6):
        pet.birthday()
        if pet.age <= 3:
            pet.grow(0.25)
            pet.say(f"I am {pet.age} and still growing!")
        else:
            pet.say(f"I am {pet.age}. I stopped growing at 3.")

    # -----------------------------------------------------
    # 5. A COUNTER
    #    Make a box, then add to it every time round.
    # -----------------------------------------------------
    steps_taken = 0
    for i in range(3):
        pet.step()
        steps_taken = steps_taken + 1      # or:  steps_taken += 1
    show("steps_taken", steps_taken)
    pet.say(f"I took {steps_taken} steps in total.")

    # -----------------------------------------------------
    # 6. A WHILE LOOP  -  keep going UNTIL something changes
    #    Careful: if the thing never changes, it loops forever!
    # -----------------------------------------------------
    energy = 3
    while energy > 0:
        pet.jump()
        energy = energy - 1                # <- this is what saves us
        show("energy", energy)
    pet.say("Out of energy. Nap time.")
    pet.sleep(1)
    pet.wake()

    # -----------------------------------------------------
    # 7. A LOOP INSIDE A LOOP
    #    The inside loop finishes completely, every single
    #    time the outside loop goes round once.
    # -----------------------------------------------------
    pet.turn()
    for round_number in range(2):
        for beat in range(2):
            pet.jump()
        pet.spin()
    pet.turn()

    # =====================================================
    #   YOUR TURN
    # =====================================================

    # CHALLENGE 1 (easy)
    # Change the loop in part 1 so the pet takes 6 steps.
    # What happens when it reaches the fence?

    # CHALLENGE 2 (easy)
    # Use a loop to make the pet jump 5 times,
    # then use another loop to make it spin 3 times.

    # CHALLENGE 3 (medium)  -  COUNTDOWN
    # Use range(5, 0, -1) to count down 5, 4, 3, 2, 1
    # with pet.say(), then pet.cheer() for "Lift off!"

    # CHALLENGE 4 (medium)  -  THE PATROL
    # Make the pet walk 5 steps forward, turn, walk 5 steps
    # back, and do that whole patrol 2 times.
    # Hint: a loop inside a loop.

    # CHALLENGE 5 (medium)  -  TREAT COUNTER
    # Start with treats = 0.
    # Loop 6 times: each time the pet eats and treats goes up 1.
    # After the loop, say how many treats it ate.

    # CHALLENGE 6 (tricky)  -  EVERY SECOND STEP
    # Loop from 1 to 10. On EVEN numbers the pet jumps,
    # on ODD numbers it steps.
    # Hint: a number is even when   number % 2 == 0

    # BOSS CHALLENGE (*)  -  THE PET OLYMPICS
    # Build a routine with at least 3 loops and 1 if statement.
    # It must include: a countdown, a walk, a dance,
    # and a victory cheer at the end.
    # Then show it to the room!


run(main)
