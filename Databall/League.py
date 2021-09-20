from Match import *
from GameObjects import *


class League:

    def __init__(self, league_name):
        self.league_name = league_name
        self.matches = []
        self.played_matches = []
        self.winners = []  # Teams that go through to the next round
        self.tournament_in_play = True
        self.__tournament_winner = None

        teams = GameObjects().Teams.copy()
        # Add teams to tournament, select opponent
        while len(teams) > 0:
            idx = random.randint(0, len(teams)-1)
            team1 = teams[idx]
            teams.remove(team1)

            idx = random.randint(0, len(teams)-1)
            team2 = teams[idx]
            teams.remove(team2)

            self.matches.append(Match(team1, team2))

    def add_team(self, team):
        self.teams.append(team)

    def get_played_matches(self):
        return self.played_matches()

    def get_match(self):
        return self.matches

    def play_match(self):
        # Tournament over - cannot play match
        if not self.tournament_in_play:
            return

        current_match = self.matches[0]
        current_match.play_match()
        print(current_match.print_match_details())
        self.matches.remove(current_match)
        self.played_matches.append(current_match)
        self.winners.append(current_match.winner)

        # Next stage of tournament - progress the winners
        if len(self.matches) == 0:
            # Check if tournament has ended (1 winner left)
            if len(self.winners) == 1:
                self.tournament_in_play = self.winners[0]
                self.tournament_in_play = False
                return

            while len(self.winners) > 0:
                idx = random.randint(0, len(self.winners)-1)
                team1 = self.winners[idx]
                self.winners.remove(team1)

                idx = random.randint(0, len(self.winners)-1)
                team2 = self.winners[idx]
                self.winners.remove(team2)
                self.matches.append(Match(team1, team2))


    def add_match(self, match):
        self.matches.append(match)

    @property
    def winner(self):
        return self.__tournament_winner


t = League("T1")
while t.tournament_in_play:
    match = t.play_match()