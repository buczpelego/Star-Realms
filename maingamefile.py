from numpy import sort
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
    print('Player HP: ' + str(player1.health))
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
            print('Player HP: ' + str(player1.health))
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
                    elif player_input > 0 and player_input <= len(market_place.cardlist): #kupowanie karty z marketu
                        chosen_card = market_place.cardlist[player_input - 1]
                        if player_total_gold < chosen_card.cost:
                            print('not enough gold to buy ' + str(chosen_card.name))
                        else:
                            player_total_gold -= chosen_card.cost
                            chosen_card.change_location(market_place, player1.discard)
                            if len(market_deck.cardlist) > 0:
                                market_deck.cardlist[-1].change_location(market_deck, market_place)
                            else:
                                pass
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
                        continue
                else:
                    cpu.health -= player_total_damage #od tąd wchodzi zadawanie obrażeń przeciwnikowi
                    print('Enemy Health Pool: ' +str(cpu.health))
                for i in range(len(player1.hand.cardlist)):
                    player1.hand.cardlist[-1].change_location(player1.hand, player1.discard)
                for i in range(len(player1.playarea.cardlist)):
                    player1.playarea.cardlist[-1].change_location(player1.playarea, player1.discard)    
                for i in range(5): #dobranie kart z deku do ręki
                    player1.deck.cardlist[-1].change_location(player1.deck, player1.hand)
                    if len(player1.deck.cardlist) > 0:
                        continue
                    else: #warunek w przypadku końca kart w deku - przeniesienie i przetasowanie kart z discardu do decku
                        for i in range(len(player1.discard.cardlist)):
                            player1.discard.cardlist[-1].change_location(player1.discard, player1.deck)
                        random.shuffle(player1.deck.cardlist)             
                break
        player_input = input('press any key')
        break
    #TURA CPU
    os.system('cls')
    print('CPU Turn')
    print('CPU HP: ' +str(cpu.health))
    for i in range(len(cpu.hand.cardlist)):
        cpu.hand.cardlist[-1].change_location(cpu.hand, cpu.playarea)
    cpu_total_gold = [card.gold for card in cpu.playarea.cardlist]
    cpu_total_gold = sum(cpu_total_gold)
    cpu_total_damage = [card.damage for card in cpu.playarea.cardlist]
    cpu_total_damage = sum(cpu_total_damage)
    print(cpu.playarea)
    print('CPU gold: ' + str(cpu_total_gold))
    print('CPU damage: ' + str(cpu_total_damage))
    print(market_place)
    player_input = input('press any key')
    os.system('cls')

    #mechanika kupna karty przez CPU:
    if len(market_place.cardlist) > 0:   
        cards_avalible_to_buy = []
        for card in market_place.cardlist: #wybór spośród kart w markecie które meżna kupić za posiadaną ilość cpu_total_gold i dodanie do osobnej listy
            if card.cost <= cpu_total_gold:
                cards_avalible_to_buy.append(card)
            else:
                pass #! może być błąd
        if len(cards_avalible_to_buy) > 0:
            sorted_cards_avalible_to_buy = sorted(cards_avalible_to_buy, key=lambda x: x.cost, reverse = True)    #posortowana lista kart mozliwych do kupienia przez CPU od najdroższej.
            while cpu_total_gold > 0:
                if sorted_cards_avalible_to_buy[0].cost <= cpu_total_gold: #jeśli pierwsza karta na liście kosztuje mniej lub tyle co cpu_total_gold to cpu ją kupuje, zmienia lokację na discard i dodaje kartę do marketu, pętla wraca do początku
                    print('CPU Turn')
                    print('CPU HP: ' +str(cpu.health))
                    print(market_place)
                    print('CPU gold left: ' + str(cpu_total_gold))
                    chosen_card = sorted_cards_avalible_to_buy[0]
                    market_place.cardlist[sorted_cards_avalible_to_buy.index(chosen_card)].change_location(market_place, cpu.discard)
                    cpu_total_gold -= chosen_card.cost                      #po zakupie, cpu_total_gold zostaje zmniejszone o koszt kupionej karty
                    if len(market_deck.cardlist) > 0: 
                        market_deck.cardlist[-1].change_location(market_deck, market_place)
                    else:
                        break
                    print('CPU bought ' + str(chosen_card))
                    player_input = input('CPU gold left: ' + str(cpu_total_gold))
                    os.system('cls')
                    continue
                elif sorted_cards_avalible_to_buy[0].cost > cpu_total_gold: #jeśli pierwsza karta na liście kosztuje więcej niż cpu total_gold, usuwa ją z listy i wraca do początku pętli
                    sorted_cards_avalible_to_buy.remove(sorted_cards_avalible_to_buy[0])
                    continue
                elif len(sorted_cards_avalible_to_buy) == 2 and sorted_cards_avalible_to_buy[0].cost == 3 and sorted_cards_avalible_to_buy[1] == 1 and cpu_total_gold == 2: #warunek kupienia Odkrywcy przez CPU
                    print('CPU Turn')
                    print('CPU HP: ' +str(cpu.health))
                    print(market_place)
                    print('CPU gold left: ' + str(cpu_total_gold))
                    chosen_card = explorer_deck[0]
                    chosen_card.change_location(explorer_deck, cpu.discard)
                    cpu_total_gold -= chosen_card.cost
                    print('CPU bought ' +str(chosen_card))
                    player_input = input('CPU gold left: ' + str(cpu_total_gold))
                    os.system('cls')
                    continue
                elif len(sorted_cards_avalible_to_buy) == 2 and cpu_total_gold > 0: #wyzerowanie cpu_total_gold w przypadku braku możliwych kart do kupienia i posiadania niewykorzystanego złota
                    cpu_total_gold = 0
                    os.system('cls')
                    continue
                else: #przerwanie pętli w przypadku braku możliwych kart do kupienia i braku złota
                    break
        else:
            pass            
    else:
        pass
    
    player1.health -= cpu_total_damage
    for i in range(len(cpu.playarea.cardlist)):
        cpu.playarea.cardlist[-1].change_location(cpu.playarea, cpu.discard)
    for i in range(5):
        cpu.deck.cardlist[-1].change_location(cpu.deck, cpu.hand)
        if len(cpu.deck.cardlist) > 0:
            continue
        else:
            for i in range(len(cpu.discard.cardlist)):
                cpu.discard.cardlist[-1].change_location(cpu.discard, cpu.deck)
            random.shuffle(cpu.deck.cardlist)     

if player1.health <= 0:
    print('Player 1 lost')
elif cpu.health <= 0:
    print('Player 1 win')


# WERSJA STABILNA!