from a_Players import *

class Teams:

    def __init__(self, team_name, team_budget):
        self.team_name = team_name
        self.team_budget = team_budget
        self.players = []
        self.team_score = 0

        for player in self.players:
            self.team_score += player.score

    def add_player(self, player):
        self.players.append(player)

    def get_budget(self):
        return self.team_budget

    def get_name(self):
        return self.team_name

    def get_player_list(self):
        return self.players
