from classobject import *
from cards import *
import os
player1 = Player('Player 1')
cpu = Player('CPU')
market_deck = Area('Market Deck')
market_deck.cardlist.extend([mothership1, blob_destroyer1, blob_fighter1, war_blob1, imperial_frigate1, imperial_frigate2, comodity_ferry1, comodity_ferry2,
                             imperial_fighter1, imperial_merchant1, battle_bark1, science_ship1, mega_towboat1, mercantile_boat1, mercantile_boat2, cutter1, embassy_yacht1, cargo_ship1,
                             patrol_bot1, patrol_bot2, defensive_bot1, supply_bot1, supply_bot2, mercantile_bot, battle_mech])
random.shuffle(market_deck.cardlist)
market_place = Area('Market Place')
market_counter = 0
while market_counter < 5:
    market_place.cardlist.append(market_deck.cardlist.pop())
    market_counter += 1
cards_bin = Area('Cards bin')

while player1.health > 0 and cpu.health > 0:
    print("PLAYER TURN")
    print(player1.hand)
    print(player1.playarea)
    while True:
        player_input = input('Select card to play by index. Press "P" to proceed').upper()
        if player_input.isnumeric() == False and player_input != 'P':
            continue
        elif player_input.isnumeric() == True:
            player_input = int(player_input)
            if player_input < 1 or player_input > len(player1.hand.cardlist):
                continue
            else:
                chosen_card = player1.hand.cardlist[player_input - 1]
                print(chosen_card)
                chosen_card.change_location(player1.hand, player1.playarea)
                os.system('cls')
                print('PLAYER TURN')
                print(player1.hand)
                print(player1.playarea)
                total_damage = [card.damage for card in player1.playarea.cardlist]
                total_damage = sum(total_damage)
                print('TOTAL DAMAGE: '+ str(total_damage))
                total_gold = [card.gold for card in player1.playarea.cardlist]
                total_gold = sum(total_gold)
                print('TOTAL GOLD: ' + str(total_gold))
                continue
        else:
            print('udało się procedować')
            break
    break


#Opracować zadawanie obrażeń i kupowanie kart.