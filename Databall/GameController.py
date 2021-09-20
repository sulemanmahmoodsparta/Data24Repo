import random

from GameObjects import GameObjects
from Match import Match


# Decorator function to force class to be singleton
def singleton(cls, *args, **kw):
    instances = {}

    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


# Decorator function to print a banner before and after
def banner(func):
    def _banner(*args, **kwargs):
        print(f"\n{'=' * 50}")
        func(*args, **kwargs)
        print(f"{'=' * 50}\n")

    return _banner



@singleton
class GameController:
    __game_states = [
        "Starting"
        , "Main Menu"
    ]

    def __init__(self):
        self.print_banner("DataBall 24")

        # Set game running flag to true for infinite loop
        self.game_is_running = True

        # Select manager name
        self.__gamer_name = input("Enter your (manager) name: ")

        # Create teams and players
        self.__game_objects = GameObjects()

        # Allow gamer to select team to manage
        print("What team would you like to manage? ")
        teams = self.__game_objects.Teams
        for i in range(1, len(teams)):
            print(f"{i}. {teams[i].team_name}")
        self.__team = input("Please enter your team number: ")
        self.__team = teams[int(self.__team)]

        # Game state
        self.state = "Starting"

    def run_game(self):
        print("Starting loop")

        self.print_banner(f"Welcome {self.__gamer_name}!\n"
              f"You are now the proud manager of {self.__team.team_name}")

        i = 0
        while self.game_is_running:
            i += 1
            if i > 10:
                self.game_is_running = False

            # Play a match - generate an opponent
            match = GameObjects().generate_match(self.__team)
            match.print_match_details()

        print("Ending loop")

    @property
    def GameObjects(self):
        return type(self).__gameObjects

    @staticmethod
    @banner
    def print_banner(txt: str):
        print(txt)

    @property
    def Team(self):
        return self.__team

# Test Code
GameController().run_game()
