# =========================================================
#   TEACHER SOLUTIONS  -  SESSION 4
#   Includes one full "final project" example at the bottom.
# =========================================================

from petpal import *
import random


def celebrate(pet):
    """CHALLENGE 1"""
    pet.jump()
    pet.spin()
    pet.cheer()


def grow_up(pet, years):
    """CHALLENGE 3 - a function with a loop AND an if inside."""
    for year in range(years):
        pet.birthday()
        if pet.age < 4:
            pet.grow(0.25)
            pet.say(f"{pet.age} years old and growing!")
        else:
            pet.say(f"{pet.age} years old - fully grown.")


def is_old(age):
    """CHALLENGE 4 - returns a bool."""
    return age >= 10


def do_trick(pet, trick_name):
    pet.say("Watch this: " + trick_name)
    if trick_name == "jump":
        pet.jump()
    elif trick_name == "spin":
        pet.spin()
    elif trick_name == "dance":
        pet.dance()
    else:
        pet.sit()


def main():
    pet = Pet("dog")
    pet.name = "Nova"
    pet.color = "lavender"
    pet.age = 1
    pet.size = 0.8

    # CHALLENGE 1
    celebrate(pet)

    # CHALLENGE 2 - a longer list
    tricks = ["jump", "spin", "dance", "sit", "roll"]
    show("tricks", tricks)
    for trick in tricks:
        do_trick(pet, trick)

    # CHALLENGE 3
    grow_up(pet, 6)

    # CHALLENGE 4
    show("is_old", is_old(pet.age))
    if is_old(pet.age):
        pet.say("I am a wise old dog.")
    else:
        pet.say("Still a youngster!")

    # CHALLENGE 5 - random taste test
    foods = ["broccoli", "chicken", "cheese", "banana", "lettuce"]
    for food in foods:
        likes_it = random.choice([True, False])
        if likes_it:
            pet.say(f"{food}? Yes please!")
            pet.eat()
        else:
            pet.think(f"{food}? No thank you.")

    # =====================================================
    #   EXAMPLE FINAL PROJECT:  A DAY IN THE LIFE
    # =====================================================
    pet.say("--- A Day In The Life ---")

    pet.name = ask("What is your pet called today?")
    energy = 5
    happiness = 0

    activities = ["walk", "nap", "snack", "play"]

    for hour in range(4):
        what = random.choice(activities)
        print("Hour", hour, "->", what)

        if what == "walk":
            for i in range(3):
                pet.step()
            energy = energy - 2
            happiness = happiness + 2
        elif what == "nap":
            pet.sleep(1)
            pet.wake()
            energy = energy + 3
        elif what == "snack":
            pet.eat()
            energy = energy + 1
            happiness = happiness + 1
        else:
            pet.dance()
            energy = energy - 1
            happiness = happiness + 3

        show("energy", energy)
        show("happiness", happiness)
        pet.turn()

    if happiness >= 5:
        pet.say(f"What a day! {pet.name} is very happy.")
        celebrate(pet)
    else:
        pet.say("A quiet day. Same time tomorrow?")


run(main)
