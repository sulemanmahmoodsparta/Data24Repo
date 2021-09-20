from s_Teams import Teams
import random


class Match:
    def __init__(self, team1: Teams, team2: Teams):
        self.team1 = team1
        self.team2 = team2
        self.winner = None  # determined after play_match is called

    def play_match(self):
        # Determine which teams wins the match. Team 2 is favoured when its comes to draws.
        if self.team1.team_score + random.randint(-5, 5) > self.team2.team_score + random.randint(-5, 5):
            self.winner = self.team1
            self.team1.team_budget += random.randint(5, 10)
            self.team2.team_budget += random.randint(1, 3)
            # print(f"Your new budget is {self.team1.team_budget}")
        else:
            self.winner = self.team2
            self.team2.team_budget += random.randint(5, 10)
            self.team1.team_budget += random.randint(1, 3)

    def match_result(self):
        return self.winner

    def add_points(self):
        pass

    def print_match_details(self):
        teams = f"{self.team1.team_name} is playing against {self.team2.team_name}"
        result = " "
        if self.winner is not None:
            result = f": {self.winner.team_name} won"

        print(f"{teams}{result}")
