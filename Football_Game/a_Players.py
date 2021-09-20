import random # for player generation
from abc import ABC, abstractmethod

PlayerPositions = ["Goalkeeper", "Defender", "Midfielder", "Attacker"]

# An Abstract class that cannot be initialised
class Players(ABC):
    @abstractmethod
    def __init__(self, fname, lname, value, position, score):
        self.id = 0
        self.first_name = fname
        self.last_name = lname
        self.value = value
        self.position = position
        self.score = score


class Goalkeeper(Players):
    # Overriding base class abstract initialiser
    def __init__(self, fname, lname, value, score):
        super().__init__(fname, lname, value, "Goalkeeper", score)


class Defender(Players):
    # Overriding base class abstract initialiser
    def __init__(self, fname, lname, value, score):
        super().__init__(fname, lname, value, "Defender", score)


class Midfielder(Players):
    # Overriding base class abstract initialiser
    def __init__(self, fname, lname, value, score):
        super().__init__(fname, lname, value, "Midfielder", score)


class Striker(Players):
    # Overriding base class abstract initialiser
    def __init__(self, fname, lname, value, score):
        super().__init__(fname, lname, value, "Striker", score)

















# Random Name Generation
fnames = ["Liam", "Noah", "Oliver", "Elijah", "William",
          "James", "Benjamin", "Lucas", "Henry", "Alexander",
          "Albert", "Ake", "Alf", "Alfons", "Alfred", "Alrik",
          "Anders","Ankers", "Annar", "Axel", "Basmus", "Christian",
          "Clemens", "David", "Davin","Felipe", "Gabrio", "Hector",
          "Helio", "Hugo", "Ismael", "Jago", "Patricio", "Ras", "Sancho",
          "Valentino", "Zacarias", "Alessandro", "Alexius", "Emiliano",
          "Gianni", "Leonardo", "Marco", "Patrick", "Roberto"]

lnames = ["Smith","Jones","Brown","Taylor","Wilson",
          "Davies","Evans","Johnson","Thomas","Roberts",
          "Silva", "Garcia", "Martin", "Murphy","Hansen", "Johansson",
          "Korhonen", "Jensen", "De Jong", "Peeters", "Müller",
          "Gruber", "Rossi", "Borg", "Novák", "Horvath", "Nowak",
          "Kazlauskas", "Bērziņš", "Ivanov", "Zajac", "Melnyk",
          "Popa", "Nagy", "Novak", "Horvat","Petrović", "Hodžić",
          "Dimitrov", "Papadopoulos","Öztürk", "Conti", "Costa",
          "Mancini", "Giordano", "Rizzo"]


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
