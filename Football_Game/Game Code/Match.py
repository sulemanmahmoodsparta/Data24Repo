from s_Teams import Teams

class Match:
    def __init__(self, team1: Teams, team2: Teams):
        self.team1 = team1
        self.team2 = team2
        self.winner = None  # determined after play_match is called

    def play_match(self):
        # For now Team1 always wins
        self.winner = self.team1

    def match_result(self):
        return self.winner

    def add_points(self):
        pass
