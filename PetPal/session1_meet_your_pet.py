# =========================================================
#   SESSION 1  -  MEET YOUR PET
#   Today: variables, and the 4 types  str  int  float  bool
#
#   HOW TO RUN: press the Run button in your editor,
#   or type in the terminal:   python session1_meet_your_pet.py
# =========================================================

from petpal import *          # this gives us Pet, run, say, ask...


def main():

    # -----------------------------------------------------
    # 1. CREATE YOUR PET
    #    A variable is a labelled box. This box is called
    #    "pet" and we put a brand new dog inside it.
    # -----------------------------------------------------
    pet = Pet("dog")           # TRY IT: change "dog" to "cat"

    # -----------------------------------------------------
    # 2. A NAME is text  ->  type: str  (short for "string")
    #    Strings ALWAYS wear quote marks: "like this"
    # -----------------------------------------------------
    pet.name = "Mochi"         # TRY IT: name your own pet

    # -----------------------------------------------------
    # 3. AN AGE is a whole number  ->  type: int
    #    No quote marks on numbers!
    # -----------------------------------------------------
    pet.age = 2

    # -----------------------------------------------------
    # 4. A SIZE can have a decimal point  ->  type: float
    #    1.0 is normal size, 2.0 is huge, 0.5 is tiny.
    # -----------------------------------------------------
    pet.size = 1.0             # TRY IT: 0.6  or  1.8

    # -----------------------------------------------------
    # 5. TRUE or FALSE  ->  type: bool  (short for "boolean")
    #    Capital T, capital F. No quote marks.
    # -----------------------------------------------------
    pet.is_hungry = True

    # -----------------------------------------------------
    # 6. A COLOUR is a string too.
    #    Try: pink lavender mint sky peach cream ginger
    #         chocolate grey white black yellow red purple
    # -----------------------------------------------------
    pet.color = "golden"

    # -----------------------------------------------------
    # 7. MAKE IT TALK
    #    + glues two strings together.
    # -----------------------------------------------------
    pet.say("Hi! My name is " + pet.name)

    # An f-string is the easy way to mix words and numbers.
    # Put an f before the quote, then {variables} in curly braces.
    pet.say(f"I am {pet.age} years old and my size is {pet.size}.")

    # print() writes in the Console panel instead of a speech bubble.
    print("The pet's name is", pet.name)

    # -----------------------------------------------------
    # 8. MOVE!
    # -----------------------------------------------------
    pet.step()
    pet.jump()
    pet.wag()

    # =====================================================
    #   YOUR TURN
    # =====================================================

    # CHALLENGE 1 (easy)
    # Change the name, age, size and colour to make the pet
    # YOURS. Run it and watch what changes.

    # CHALLENGE 2 (easy)
    # Make a variable of your own and show it on the
    # Variables panel. Delete the # at the start of these lines:
    #
    # favourite_food = "strawberries"
    # show("favourite_food", favourite_food)
    # pet.say("I love " + favourite_food)

    # CHALLENGE 3 (medium)
    # Make the pet say its whole profile in ONE sentence
    # using an f-string, like:
    #   "I am Mochi, a 2 year old dog, and my size is 1.0"
    # Write it below:


    # CHALLENGE 4 (medium)
    # Make a variable called  treats  and set it to 5 (an int).
    # Then make a variable  treats_left  that is treats - 2.
    # show() both of them and make the pet say how many are left.


    # CHALLENGE 5 (tricky - this one has a secret)
    # Try this line and see what happens:
    #     pet.say("I am " + pet.age + " years old")
    # It BREAKS. Read the Console to find out why,
    # then fix it two different ways:
    #   a) with str(pet.age)
    #   b) with an f-string


    # BOSS CHALLENGE (*)
    # Make your pet walk to stone number 4, jump, turn around,
    # walk back to stone 1, and say goodbye with its name in it.


run(main)                      # <- this line starts the show. Keep it last!
