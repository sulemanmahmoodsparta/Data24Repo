from GameController import GameController

class transfer_market:
    def __init__(self):
        self.players = []

    def buy_player(self,players,):
        self.players.remove(players) # Removing players to the transfer market.
        GameController().Team.add_player(players) # Adds player to the team.
        GameController().Team.team_budget()