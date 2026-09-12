# =========================================================
#   TRICKS - PROGRAMMER B
#
#   THIS FILE BELONGS TO ONE PERSON ONLY.
#   Rename it to your own name in Session 5:
#       git mv tricks_b.py tricks_mia.py
#   (and change the import at the top of park.py to match)
#
#   Nobody else edits this file. That is the whole point:
#   when two people work on different files, git can put
#   your work together without either of you losing anything.
# =========================================================


def warm_up(pet):
    """Called at the start of the show."""
    pet.say(f"{pet.name} is ready!")
    pet.wag()


def signature_move(pet):
    """Your one special trick. Make it good."""
    pet.dance()
    pet.jump()


def take_a_bow(pet):
    """Called at the end of the show."""
    pet.say("Was that as good as it looked?")
    pet.sit()


# TODO (Session 5): add a third trick of your own down here,
# then commit it. Your partner will pull it and it will just
# appear in the show - you never have to send her a file.
