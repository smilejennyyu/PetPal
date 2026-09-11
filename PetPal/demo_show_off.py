# =========================================================
#   PETPAL DEMO  -  run this first, just to see what happens
#   (You will be able to write all of this by Session 4!)
# =========================================================

from petpal import *


def brag(pet, thing):
    """A function! It teaches ANY pet to brag about ANY thing."""
    pet.say("Watch me " + thing + "!")


def main():
    pet = Pet("dog")
    pet.name = "Biscuit"
    pet.color = "golden"
    pet.age = 1
    pet.size = 0.8

    pet.say("Hi! I am Biscuit and I am 1 year old.")

    # A for loop: take 3 steps
    brag(pet, "walk")
    for step_number in range(3):
        pet.step()

    # An if statement: eat only when hungry
    pet.is_hungry = True
    if pet.is_hungry:
        pet.say("I am starving!")
        pet.eat()

    # A loop + an if statement: grow up, but only until age 3
    for year in range(4):
        pet.birthday()
        if pet.age <= 3:
            pet.grow(0.25)
        else:
            pet.say("All grown up. I stop growing now.")

    # A list of tricks
    tricks = ["spin", "jump", "dance"]
    for trick in tricks:
        brag(pet, trick)
        if trick == "spin":
            pet.spin()
        elif trick == "jump":
            pet.jump()
        else:
            pet.dance()

    pet.turn()
    pet.walk(2)
    pet.cheer()
    pet.say("Your turn. Let's write some Python!")


run(main)
