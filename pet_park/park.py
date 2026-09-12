# =========================================================
#   PET PARK  -  a show with two pets, written by two people
#
#   This file is shared. BOTH of you edit it, which means:
#       git pull   BEFORE you start editing
#       git push   AS SOON AS you finish
#
#   Your own tricks live in your own file. This one just
#   runs the show.
# =========================================================

from petpal import *

import tricks_a          # <- change to your partner's file name
import tricks_b          # <- change to your file name


def main():

    # ---- the performers ---------------------------------
    pet_a = Pet("dog")
    pet_a.name = "Pet A"          # TODO: your partner's pet
    pet_a.color = "golden"
    pet_a.age = 2

    pet_b = Pet("cat")
    pet_b.name = "Pet B"          # TODO: your pet
    pet_b.color = "lavender"
    pet_b.age = 2

    # ---- the show ---------------------------------------
    pet_a.say("Welcome to Pet Park!")

    tricks_a.warm_up(pet_a)
    tricks_b.warm_up(pet_b)

    for round_number in range(2):
        tricks_a.signature_move(pet_a)
        tricks_b.signature_move(pet_b)

    # a race to the fence - whoever is further along wins
    pet_a.walk(5)
    pet_b.walk(3)

    tricks_a.take_a_bow(pet_a)
    tricks_b.take_a_bow(pet_b)

    pet_b.say("Same time next week?")


run(main)
