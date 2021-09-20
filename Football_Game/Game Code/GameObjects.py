from a_Players import *
from s_Teams import Teams
import random


# Decorator function to force class to be singleton
# Credit: https://stackoverflow.com/questions/42237752/single-instance-of-class-in-python
def singleton(cls, *args, **kw):
    instances = {}

    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@singleton
class GameObjects:
    __fnames = ["Liam", "Noah", "Oliver", "Elijah", "William",
                "James", "Benjamin", "Lucas", "Henry", "Alexander"]

    __lnames = ["Smith", "Jones", "Brown", "Taylor", "Wilson",
                "Davies", "Evans", "Johnson", "Thomas", "Roberts"]

    def __init__(self):
        # Teams - A dictionary of all teams
        # TODO change this to a list
        self.teams = [
            Teams("Manchester United", 100)
            , Teams("Manchester City", 120)
            , Teams("Liverpool FC", 80)
            , Teams("Aston Villa", 50)
            , Teams("West Ham", 60)
            , Teams("Chelsea", 120)
            , Teams("Leicester City", 60)
            , Teams("Data", 500)
        ]
        self.team1 = self.teams[1]

        # A list of all the players
        self.players = []

        # Add players to the teams
        for team in self.teams:
            # Generate one goalkeeper
            player = self.__generate_player(Goalkeeper)
            self.players.append(player)
            team.add_player(player)

            # Generate 4 defenders
            for i in range(4):
                player = self.__generate_player(Defender)
                self.players.append(player)
                team.add_player(player)

            # Generate 3 Midfielders
            for i in range(3):
                player = self.__generate_player(Midfielder)
                self.players.append(player)
                team.add_player(player)

            # Generate 3 Strikers
            for i in range(4):
                player = self.__generate_player(Striker)
                self.players.append(player)
                team.add_player(player)

    @staticmethod
    def __generate_player(position):
        # Argument type invalid, cannot generate a Player of type requested
        if not issubclass(type(position), type(Players)):
            return None

        # Generate a random number as an index to determine first name
        index = random.randint(0, len(fnames) - 1)
        fname = fnames[index]

        # Generate a random number as an index to determine last name
        index = random.randint(0, len(lnames) - 1)
        lname = lnames[index]

        # Players value
        value = random.randint(75, 125)

        # position is a (sub)class object of type Player
        return position(fname, lname, value)

    @property
    def Teams(self):
        return self.teams

    @property
    def TeamNameList(self):
        return [t.team_name for t in self.teams.values()]

    @property
    def Players(self):
        return self.players


# Test
# print("Testing GameObjects.py")
# go = GameObjects()
# # for player in go.Players:
# #     print(player.first_name)
# for t in go.Teams:
#     print(t.team_name)