# =========================================================
#   TEACHER SOLUTIONS  -  SESSION 1
#   (Girls: no peeking until you've had a proper go!)
# =========================================================

from petpal import *


def main():
    pet = Pet("cat")

    # CHALLENGE 1 - make it yours
    pet.name = "Mochi"
    pet.age = 2
    pet.size = 1.0
    pet.color = "lavender"
    pet.is_hungry = True

    # CHALLENGE 2 - your own variable
    favourite_food = "strawberries"
    show("favourite_food", favourite_food)
    pet.say("I love " + favourite_food)

    # CHALLENGE 3 - the whole profile in one f-string
    pet.say(f"I am {pet.name}, a {pet.age} year old cat, "
            f"and my size is {pet.size}")

    # CHALLENGE 4 - treats maths
    treats = 5
    treats_left = treats - 2
    show("treats", treats)
    show("treats_left", treats_left)
    pet.say(f"I ate 2 treats. {treats_left} left!")

    # CHALLENGE 5 - the famous type error, fixed two ways
    # BROKEN:  pet.say("I am " + pet.age + " years old")
    pet.say("I am " + str(pet.age) + " years old")      # fix a
    pet.say(f"I am {pet.age} years old")                # fix b

    # BOSS CHALLENGE - a little journey
    pet.walk(4)
    pet.jump()
    pet.turn()
    pet.walk(3)
    pet.say(f"Goodbye from {pet.name}!")
    pet.wag()


run(main)
