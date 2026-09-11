# =========================================================
#   SESSION 4  -  FUNCTIONS, LISTS AND YOUR OWN GAME
#   Today: def, parameters, return, lists, random,
#          and then you build whatever you want.
# =========================================================

from petpal import *
import random                 # a toolbox of surprises


# =========================================================
#  FUNCTIONS LIVE OUT HERE, ABOVE main()
#  A function is a trick you teach Python ONCE and then
#  use as many times as you like.
# =========================================================

def greet(pet):
    """Say hello. 'pet' is a parameter: the pet to greet with."""
    pet.say(f"Hello! I am {pet.name} and I am {pet.age}.")
    pet.wag()


def do_trick(pet, trick_name):
    """Two parameters: which pet, and which trick."""
    pet.say("Watch this: " + trick_name)
    if trick_name == "jump":
        pet.jump()
    elif trick_name == "spin":
        pet.spin()
    elif trick_name == "dance":
        pet.dance()
    else:
        pet.think("I don't know that one yet.")


def years_to_dog_years(age):
    """This function RETURNS a value - it hands an answer back."""
    return age * 7


def main():

    # -----------------------------------------------------
    # 1. USING YOUR FUNCTIONS
    # -----------------------------------------------------
    pet = Pet("dog")
    pet.name = "Nova"
    pet.color = "lavender"
    pet.age = 3

    greet(pet)                       # one line instead of three
    do_trick(pet, "spin")
    do_trick(pet, "jump")

    # -----------------------------------------------------
    # 2. RETURN  -  a function that gives an answer back
    # -----------------------------------------------------
    dog_age = years_to_dog_years(pet.age)
    show("dog_age", dog_age)
    pet.say(f"In dog years I am {dog_age}!")

    # -----------------------------------------------------
    # 3. LISTS  -  one box that holds many things.
    #    Square brackets, commas between items.
    #    The FIRST item is number 0. (Programmers are odd.)
    # -----------------------------------------------------
    tricks = ["jump", "spin", "dance"]
    show("tricks", tricks)

    print("The first trick is", tricks[0])
    print("There are", len(tricks), "tricks")

    # -----------------------------------------------------
    # 4. A LOOP OVER A LIST  (no range() needed!)
    # -----------------------------------------------------
    for trick in tricks:
        do_trick(pet, trick)

    # You can add to a list while the program runs:
    tricks.append("sit")
    show("tricks", tricks)

    # -----------------------------------------------------
    # 5. RANDOM  -  let the computer surprise you
    # -----------------------------------------------------
    lucky = random.choice(tricks)
    pet.think("Hmm, what shall I do...")
    do_trick(pet, lucky)

    dice = random.randint(1, 6)
    show("dice", dice)
    if dice > 3:
        pet.cheer()
    else:
        pet.say("Better luck next roll.")

    # -----------------------------------------------------
    # 6. A DICTIONARY  -  labels instead of numbers
    #    Great for a pet's "save file".
    # -----------------------------------------------------
    save_file = {"name": "Nova", "age": 3, "happy": True}
    show("save_file", save_file)
    print("Saved pet name:", save_file["name"])

    # =====================================================
    #   YOUR TURN
    # =====================================================

    # CHALLENGE 1 (easy)
    # Write a function called  celebrate(pet)  that makes the
    # pet jump, spin and cheer. Then call it.

    # CHALLENGE 2 (easy)
    # Add two more tricks to the tricks list and run the loop again.

    # CHALLENGE 3 (medium)
    # Write a function  grow_up(pet, years)  that loops through
    # the years, gives a birthday each year, and grows the pet
    # only while it is younger than 4. Call it with 6 years.

    # CHALLENGE 4 (medium)
    # Write a function  is_old(age)  that RETURNS True if age
    # is 10 or more, and False if not. Use it in an if statement.

    # CHALLENGE 5 (tricky)
    # Make a list of 5 foods. Loop through them. Use random to
    # decide if the pet likes each one: if it does, it eats and
    # cheers; if not, it thinks "no thanks".

    # =====================================================
    #   FINAL PROJECT:  A DAY IN THE LIFE OF ______
    #
    #   Build your own pet story or mini game. It must use:
    #     [ ] at least 3 variables, and at least 2 different types
    #     [ ] at least 1 if / elif / else
    #     [ ] at least 1 loop
    #     [ ] at least 1 function that YOU wrote
    #     [ ] at least 1 list
    #     [ ] ask() so the human can join in
    #
    #   Ideas:
    #     * a pet that wakes up, gets hungry, and goes to sleep
    #     * a training game: the human guesses the secret trick
    #     * a race: two pets (yes, you can make two!) take
    #       random numbers of steps until one reaches the fence
    #     * a birthday party that counts down and grows the pet
    #
    #   Write it below. Make it yours. Show it off at the end.
    # =====================================================


run(main)
