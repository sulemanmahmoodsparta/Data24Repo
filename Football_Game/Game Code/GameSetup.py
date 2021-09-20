"""
Put all game setup code in this file. It should contain:
1. The list of all players
2. The list of all teams
"""

from a_Players import Players, PlayerPositions
from s_Teams import Teams

# This function generates a player object
def generate_player():

    pass

# Players
players = [
    Players(fname = "A", lname = "B", value = 100, position = PlayerPositions.attacker)
    , Players(fname = "C ", lname = "D", value = 100, position = PlayerPositions.defender)
    , Players(fname = "E ", lname = "F", value = 100, position = PlayerPositions.goalkeeper)
    , Players(fname = "G ", lname = "H", value = 100, position = PlayerPositions.midfielder)
    , Players(fname = "I ", lname = "J", value = 100, position = PlayerPositions.defender)
    , Players(fname = "K ", lname = "L", value = 100, position = PlayerPositions.attacker)
    , Players(fname = "M ", lname = "N", value = 100, position = PlayerPositions.goalkeeper)
]

# Teams - A dictionary of all teams
Teams = {
    "Manchester_United": Teams("Manchester United", 100)
    , "Manchester_City": Teams("Manchester City", 120)
    , "Liverpool": Teams("Liverpool FC", 80)
    , "Aston_Villa": Teams("Aston Villa", 70)
    , "West Ham": Teams("West Ham", 60)
    , "Chelsea": Teams("Chelsea", 120)
    , "Leicester City": Teams("Leicester City", 60)
    , "Data 24": Teams("Data", 500)
}

# Populate teams with players: TODO: Implement random generation
Teams["Manchester_United"].add_player(players[0])

for team in Teams.values():
    player = generate_player("Goalkeeper")