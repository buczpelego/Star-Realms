from classobject import *
from cards import *
import os
player1 = Player('Player 1')
cpu = Player('CPU')
market_deck = Area('Market Deck') #Przygotowywanie marketu
market_deck.cardlist.extend([mothership1, blob_destroyer1, blob_fighter1, war_blob1, imperial_frigate1, imperial_frigate2, comodity_ferry1, comodity_ferry2,
                             imperial_fighter1, imperial_merchant1, battle_bark1, science_ship1, mega_towboat1, mercantile_boat1, mercantile_boat2, cutter1, embassy_yacht1, cargo_ship1,
                             patrol_bot1, patrol_bot2, defensive_bot1, supply_bot1, supply_bot2, mercantile_bot, battle_mech])
random.shuffle(market_deck.cardlist)
market_place = Area('Market Place')
market_counter = 0
while market_counter < 5:
    market_place.cardlist.append(market_deck.cardlist.pop())
    market_counter += 1
cards_bin = Area('Cards bin') #Przygotowywanie złomowiska
explorer_deck = Area('Explorer deck') # Przygotowywanie talii odkrywców
explorer_deck.cardlist.extend([explorer1, explorer2, explorer3, explorer4, explorer5, explorer6, explorer7, explorer8, explorer9, explorer10])
#R0zpoczecie gry
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
                chosen_card.change_location(player1.hand, player1.playarea)
                os.system('cls')
                print('PLAYER TURN')
                print(player1.hand)
                print(player1.playarea)
                player_total_damage = [card.damage for card in player1.playarea.cardlist]
                player_total_damage = sum(player_total_damage)
                print('TOTAL DAMAGE: '+ str(player_total_damage))
                player_total_gold = [card.gold for card in player1.playarea.cardlist]
                player_total_gold = sum(player_total_gold)
                print('TOTAL GOLD: ' + str(player_total_gold))
                continue
        else:
            #Przejście do kupowania kart z marketu
            os.system('cls')
            print('PLAYER TURN')
            print(player1.playarea)
            player_total_damage = [card.damage for card in player1.playarea.cardlist]
            player_total_damage = sum(player_total_damage)
            print('TOTAL DAMAGE: '+ str(player_total_damage))
            player_total_gold = [card.gold for card in player1.playarea.cardlist]
            player_total_gold = sum(player_total_gold)
            print('TOTAL GOLD: ' + str(player_total_gold))
            print(market_place)
            print('If you can\'t buy any card form market, you can buy Explorer (BY PRESSING - 6) for 2 gold (Explorer gives 2 gold)')
            #wybór karty z marketu
            while True: #Pętla przerywa się w momencie zakończenia kupowania kart
                player_input = input('Select card to buy by pressing index number. Press "P" to proceed').upper()
                if player_input.isnumeric() == False and player_input != 'P':
                    continue
                elif player_input.isnumeric() == True: 
                    player_input = int(player_input)
                    if player_input < 1:
                        continue
                    elif player_input == 6: #kupowanie karty odkrywcy
                        if player_total_gold < 2:
                            print('not enough gold')
                            continue
                        else:
                            if len(explorer_deck.cardlist) > 0:
                                player_total_gold -= 2
                                explorer_deck.cardlist[-1].change_location(explorer_deck, player1.discard)
                                os.system('cls')
                                print('PLAYER TURN')
                                print(player1.playarea)
                                print('TOTAL DAMAGE: '+ str(player_total_damage))
                                print('TOTAL GOLD: ' + str(player_total_gold))
                                print(market_place)
                                print('If you can\'t buy any card form market, you can buy Explorer (BY PRESSING - 6) for 2 gold (Explorer gives 2 gold)')
                                continue
                            else:
                                print('No more explorers in deck')
                                continue
                    elif player_input > 6:
                        continue
                    else: #kupowanie karty z marketu
                        chosen_card = market_place.cardlist[player_input - 1]
                        if player_total_gold < chosen_card.cost:
                            print('not enough gold to buy ' + str(chosen_card.name))
                        else:
                            player_total_gold -= chosen_card.cost
                            chosen_card.change_location(market_place, player1.discard)
                            market_deck.cardlist[-1].change_location(market_deck, market_place)
                            os.system('cls')
                            print('PLAYER TURN')
                            print(player1.playarea)
                            print('TOTAL DAMAGE: '+ str(player_total_damage))
                            print('TOTAL GOLD: ' + str(player_total_gold))
                            print(market_place)
                            print('If you can\'t buy any card form market, you can buy Explorer (BY PRESSING - 6) for 2 gold (Explorer gives 2 gold)')
                            continue
                        continue
                else:
                    break #od tąd wchodzi zadawanie obrażeń przeciwnikowi
            break
    break


#Opracować zadawanie obrażeń przeciwnikowi