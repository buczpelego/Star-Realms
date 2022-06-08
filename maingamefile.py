from classobject import *
from cards import *
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

while player1.health > 0 or cpu.health > 0:
    print("PLAYER TURN")
    print(player1.hand)
    while True:
        pass
    break

#w pliku classes dopracuj mechanikę zmiany lokacji przez karty