import random # for player generation
from abc import ABC, abstractmethod

PlayerPositions = ["Goalkeeper","Defender","Midfielder","Attacker"]

# An Abstract class that cannot be initialised
class Players(ABC):
    @abstractmethod
    def __init__(self, fname, lname, value, position):
        self.id = 0
        self.first_name = fname
        self.last_name = lname
        self.value = value
        self.position = position


class Goalkeeper(Players):
    # Overriding base class abstract initialiser
    def __init__(self, fname, lname, value):
        super().__init__(fname, lname, value, "Goalkeeper")


class Defender(Players):
    # Overriding base class abstract initialiser
    def __init__(self, fname, lname, value):
        super().__init__(fname, lname, value, "Defender")


class Midfielder(Players):
    # Overriding base class abstract initialiser
    def __init__(self, fname, lname, value):
        super().__init__(fname, lname, value, "Midfielder")


class Striker(Players):
    # Overriding base class abstract initialiser
    def __init__(self, fname, lname, value):
        super().__init__(fname, lname, value, "Striker")

















# Random Name Generation
fnames = ["Liam","Noah","Oliver","Elijah","William",
          "James","Benjamin","Lucas","Henry","Alexander"]

lnames = ["Smith","Jones","Brown","Taylor","Wilson",
          "Davies","Evans","Johnson","Thomas","Roberts"]


def generate_name():
    index = random.randint(0, len(fnames) - 1)
    fname = fnames[index]

    index = random.randint(0, len(lnames) - 1)
    lname = lnames[index]

    return fname, lname


def generate_player(position):
    fname, lname = generate_name()
    value = random.randint(75, 125)

    if position == "Goalkeeper":
        return Goalkeeper(fname, lname, value, position)

    return Players(fname,lname, value, position)
