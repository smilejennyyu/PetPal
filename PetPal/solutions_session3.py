# =========================================================
#   TEACHER SOLUTIONS  -  SESSION 3
# =========================================================

from petpal import *


def main():
    pet = Pet("dog")
    pet.name = "Pixel"
    pet.color = "peach"
    pet.age = 1
    pet.size = 0.7

    # CHALLENGE 1 - 6 steps (it bumps the fence and stops)
    for i in range(6):
        pet.step()
    pet.say("The fence stops me - the number just can't go higher.")
    pet.turn()
    pet.walk(6)
    pet.turn()

    # CHALLENGE 2 - two simple loops
    for i in range(5):
        pet.jump()
    for i in range(3):
        pet.spin()

    # CHALLENGE 3 - COUNTDOWN
    for n in range(5, 0, -1):
        pet.say(str(n))
    pet.say("Lift off!")
    pet.cheer()

    # CHALLENGE 4 - THE PATROL (a loop inside a loop)
    for patrol in range(2):
        for i in range(5):
            pet.step()
        pet.turn()
        for i in range(5):
            pet.step()
        pet.turn()

    # CHALLENGE 5 - TREAT COUNTER
    treats = 0
    for i in range(6):
        pet.eat()
        treats = treats + 1
        show("treats", treats)
    pet.say(f"I ate {treats} treats. No regrets.")

    # CHALLENGE 6 - EVERY SECOND STEP
    pet.turn()
    for number in range(1, 11):
        if number % 2 == 0:
            pet.jump()
        else:
            pet.step()
    pet.turn()

    # BOSS CHALLENGE - THE PET OLYMPICS
    pet.say("Welcome to the Pet Olympics!")
    for n in range(3, 0, -1):            # loop 1: countdown
        pet.say(str(n))
    pet.say("GO!")

    for i in range(5):                   # loop 2: the sprint
        pet.step()

    for beat in range(3):                # loop 3: the routine
        pet.jump()
        pet.spin()

    score = 10
    if score >= 8:                       # the if statement
        pet.say("GOLD MEDAL!")
        pet.dance()
        pet.cheer()
    else:
        pet.say("Good effort!")


run(main)
