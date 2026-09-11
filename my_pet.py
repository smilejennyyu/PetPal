# =========================================================
#   MY PET  -  your own playground.
#   Nothing here is homework. Try anything.
#   If you break it, that is called "learning".
# =========================================================

from petpal import *


def main():

    pet = Pet("dog")           # "dog" or "cat"
    pet.name = "Your Pet"
    pet.age = 1
    pet.size = 1.0
    pet.color = "pink"

    pet.say("Write some code and see what I do!")

    # ---- everything your pet can do -------------------
    # pet.say("hello")      pet.think("hmm")
    # pet.step()            pet.walk(3)        pet.back(2)
    # pet.turn()            pet.jump()         pet.spin()
    # pet.dance()           pet.wag()          pet.cheer()
    # pet.sit()             pet.eat()          pet.sleep(2)
    # pet.wake()            pet.wait(1)
    # pet.birthday()        pet.grow(0.2)      pet.shrink(0.1)
    #
    # pet.name  pet.age  pet.size  pet.color  pet.is_hungry  pet.mood
    #
    # show("treats", 5)     ask("What's your name?")    help_me()
    # ---------------------------------------------------

    # Your code starts here:



run(main)
