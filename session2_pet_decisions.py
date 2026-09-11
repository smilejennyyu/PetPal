# =========================================================
#   SESSION 2  -  PET DECISIONS
#   Today: comparisons, if / elif / else, and / or / not,
#          asking the user a question, changing types
# =========================================================

from petpal import *


def main():

    pet = Pet("cat")
    pet.name = "Luna"
    pet.age = 2
    pet.size = 1.0
    pet.is_hungry = True

    # -----------------------------------------------------
    # 1. COMPARING THINGS
    #    These questions always answer True or False.
    #
    #        ==   is it the same as?        (two equals!)
    #        !=   is it different from?
    #        <    less than        >   greater than
    #        <=   less or equal    >=  greater or equal
    # -----------------------------------------------------
    is_baby = pet.age < 3
    show("is_baby", is_baby)          # look at the type: bool

    # -----------------------------------------------------
    # 2. IF  -  do something only when something is True.
    #    The indented lines below "if" only run if it is True.
    #    The ":" and the indent are not optional!
    # -----------------------------------------------------
    if pet.is_hungry:
        pet.say("My bowl is empty!")
        pet.eat()

    # -----------------------------------------------------
    # 3. IF / ELSE  -  one road or the other road.
    # -----------------------------------------------------
    if pet.age < 3:
        pet.say("I am still a kitten, so I am still growing.")
        pet.grow(0.3)
    else:
        pet.say("I am all grown up. This is my final size.")

    # -----------------------------------------------------
    # 4. IF / ELIF / ELSE  -  many roads.
    #    Python checks them top to bottom and takes the
    #    FIRST one that is True. Then it stops checking.
    # -----------------------------------------------------
    pet.mood = "sleepy"

    if pet.mood == "excited":
        pet.dance()
    elif pet.mood == "sleepy":
        pet.sleep(2)
        pet.wake()
    elif pet.mood == "sad":
        pet.say("I need a hug.")
    else:
        pet.wag()

    # -----------------------------------------------------
    # 5. AND / OR / NOT  -  combining questions
    # -----------------------------------------------------
    has_energy = True

    if has_energy and not pet.is_hungry:
        pet.say("Fed and full of beans. Let's play!")
        pet.jump()

    if pet.age < 1 or pet.age > 10:
        pet.say("I need extra care.")

    # -----------------------------------------------------
    # 6. ASKING THE HUMAN A QUESTION
    #    ask() always hands back a str - even "7" is text!
    #    int("7") turns that text into the number 7.
    # -----------------------------------------------------
    answer = ask("How many treats should Luna get?")
    treats = int(answer)              # str -> int
    show("answer", answer)            # type: str
    show("treats", treats)            # type: int

    if treats > 3:
        pet.say("So many treats! I am the luckiest cat.")
        pet.cheer()
    else:
        pet.say(f"{treats} treats. That will do... for now.")

    # =====================================================
    #   YOUR TURN
    # =====================================================

    # CHALLENGE 1 (easy)
    # Change pet.mood to "excited" and run again.
    # Which branch runs now? Can you predict it BEFORE running?

    # CHALLENGE 2 (easy)
    # Ask the human for the pet's name with ask()
    # and use the answer to set pet.name.

    # CHALLENGE 3 (medium)  -  THE FEEDING MACHINE
    # Ask "How many hours since the last meal?"
    # Turn the answer into an int.
    #   more than 6  -> very hungry: say so, eat, then cheer
    #   3 to 6       -> a bit peckish: eat
    #   less than 3  -> not hungry: dance instead

    # CHALLENGE 4 (medium)  -  THE SIZE RULE
    # Write a rule that says:
    #   if the pet is younger than 3, it grows by 0.3
    #   otherwise it stays the same size
    # Then change pet.age to 5 and prove your rule works.

    # CHALLENGE 5 (tricky)
    # What is the difference between  =  and  == ?
    # Write your answer here as a comment:
    # ANSWER:

    # BOSS CHALLENGE (*)  -  PERSONALITY QUIZ
    # Ask 3 questions ("Do you like naps? yes/no" ...).
    # Give the pet 1 point for every "yes".
    # At the end use if / elif / else on the score to give the
    # pet a personality: sleepy, playful, or wild.
    # Make the pet act it out and say its personality.


run(main)
