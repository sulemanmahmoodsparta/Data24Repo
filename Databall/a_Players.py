import random # for player generation
from abc import ABC, abstractmethod

# An Abstract class that cannot be initialised
class Players(ABC):
    @abstractmethod
    def __init__(self, fname, lname, value, position, score):
        self.__first_name = fname
        self.__last_name = lname
        self.__value = value
        self.__position = position
        self.__score = score

    @property
    def name(self):
        return f"{self.__first_name} {self.__last_name}"

    @property
    def value(self):
        return self.__value

    @property
    def cost(self):
        return self.__value

    @property
    def position(self):
        return self.__position

    @property
    def score(self):
        return self.__score


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