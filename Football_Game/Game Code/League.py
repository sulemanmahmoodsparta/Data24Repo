class League():

    def __init__(self, league_name):
        self.league_name = league_name
        self.teams = []
        self.matches =[]

    def add_team(self, team):
        self.teams.append(team)

    def matches(self, team1, team2):


    def get_match(self):
        return self.matches


    def add_match(self, match):
        self.matches.append(match)
