from s_Teams import *
from a_Player_List import *


aston_villa.add_player(players[0:2])
manchester_united.add_player(players[3:5])


for p in aston_villa.get_player_list():
    print(f"{p}")