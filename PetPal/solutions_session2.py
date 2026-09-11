# =========================================================
#   TEACHER SOLUTIONS  -  SESSION 2
# =========================================================

from petpal import *


def main():
    pet = Pet("cat")
    pet.age = 2
    pet.size = 1.0

    # CHALLENGE 2 - name from the human
    pet.name = ask("What should we call this cat?")
    pet.say(f"Nice to meet you. I am {pet.name}.")

    # CHALLENGE 3 - THE FEEDING MACHINE
    hours = int(ask("How many hours since the last meal?"))
    show("hours", hours)

    if hours > 6:
        pet.say("I am STARVING. Feed me immediately.")
        pet.eat()
        pet.cheer()
    elif hours >= 3:
        pet.say("I could eat.")
        pet.eat()
    else:
        pet.say("Not hungry - let's play instead!")
        pet.dance()

    # CHALLENGE 4 - THE SIZE RULE
    pet.age = 5                     # try 2 as well, and watch the change
    show("age", pet.age)
    if pet.age < 3:
        pet.grow(0.3)
        pet.say("Still growing!")
    else:
        pet.say("Fully grown - my size stays the same.")

    # CHALLENGE 5 - the answer
    # =  puts a value INTO a box        (pet.age = 5)
    # == ASKS whether two things match  (pet.age == 5)

    # BOSS CHALLENGE - PERSONALITY QUIZ
    score = 0

    a1 = ask("Do you like long naps? (yes/no)")
    if a1 == "yes":
        score = score + 1

    a2 = ask("Do you run around at midnight? (yes/no)")
    if a2 == "yes":
        score = score + 1

    a3 = ask("Do you knock things off tables? (yes/no)")
    if a3 == "yes":
        score = score + 1

    show("score", score)

    if score == 0:
        personality = "sleepy"
        pet.sleep(2)
        pet.wake()
    elif score <= 2:
        personality = "playful"
        pet.jump()
        pet.spin()
    else:
        personality = "absolutely wild"
        pet.dance()
        pet.cheer()

    show("personality", personality)
    pet.say(f"My personality is: {personality}!")


run(main)
