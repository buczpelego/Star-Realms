# 1st comment
import pandas
import os
import sys
from termcolor import colored
from tabulate import tabulate
game_title = """

_______ _________ _______  _______    _______  _______  _______  _        _______  _______ 
(  ____ \ \__  __/(  ___  )(  ____ )  (  ____ )(  ____ \(  ___  )( \      (       )(  ____\ 
| (    \/   ) (   | (   ) || (    )|  | (    )|| (    \/| (   ) || (      | () () || (    \/
| (_____    | |   | (___) || (____)|  | (____)|| (__    | (___) || |      | || || || (_____ 
(_____  )   | |   |  ___  ||     __)  |     __)|  __)   |  ___  || |      | |(_)| |(_____  )
      ) |   | |   | (   ) || (\ (     | (\ (   | (      | (   ) || |      | |   | |      ) |
/\____) |   | |   | )   ( || ) \ \__  | ) \ \__| (____/\| )   ( || (____/\| )   ( |/\____) |
\_______)   )_(   |/     \||/   \__/  |/   \__/(_______/|/     \|(_______/|/     \|\_______)

"""
game_title = colored(game_title, 'cyan')
main_menu = {colored("MENU", 'blue'): [colored("NEW GAME", 'cyan'), colored("EXIT", 'red')], colored('key', 'blue'): [1, 2]}
main_menu = pandas.DataFrame(main_menu)
main_menu = tabulate(main_menu, headers = 'keys', tablefmt='psql', showindex=False)
print(game_title)
print(main_menu)
while True: #Pętla wyboru opcji. Wyjście z pętli to wybór 1 lub 2
    player_input = input(colored('PRESS CORRESPONDING KEY', 'cyan'))
    if player_input.isnumeric() == False:
        continue
    else:
        player_input = int(player_input)
        if player_input == 1 or player_input == 2:
            break
        else:
            continue
if player_input == 1:
    os.system('cls')
    pass
else:
    print(colored('EXITING GAME', 'red'))
    sys.exit()