import pandas, random
from termcolor import colored
from tabulate import tabulate
class GameCard:
    def __init__(self, name, color, cost, damage, gold, regen):
        self.name = name
        self.color = color
        self.cost = cost
        self.damage = damage
        self.gold = gold
        self.regen = regen
    def __repr__(self):
        return self.name
    
class Area:
    def __init__(self, name):
        self.name = name
        self.cardlist = []
        
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.gold = 0
        self.damage = 0
        self.starting_deck = []
        scout1 = GameCard("Scout", 'white', 0, 0, 1, 0)
        scout2 = GameCard("Scout", 'white', 0, 0, 1, 0)
        scout3 = GameCard("Scout", 'white', 0, 0, 1, 0)        
        scout4 = GameCard("Scout", 'white', 0, 0, 1, 0)
        scout5 = GameCard("Scout", 'white', 0, 0, 1, 0)
        scout6 = GameCard("Scout", 'white', 0, 0, 1, 0)
        scout7 = GameCard("Scout", 'white', 0, 0, 1, 0)
        scout8 = GameCard("Scout", 'white', 0, 0, 1, 0)
        viper1 = GameCard("Viper", 'white', 0, 1, 0, 0)
        viper2 = GameCard("Viper", 'white', 0, 1, 0, 0)
        self.starting_deck.extend([scout1, scout2, scout3, scout4, scout5, scout6, scout7, scout8, viper1, viper2])
        random.shuffle(self.starting_deck)
        self.deck = Area("Deck")
        self.discard = Area("Discard")
        self.hand = Area("Hand")
        self.playarea = Area ("Play Area")
        popcounter = 0
        while popcounter < 10:
            self.deck.cardlist.append(self.starting_deck.pop())
            popcounter += 1
        drawcounter = 0
        while drawcounter < 5:
            self.hand.cardlist.append(self.deck.cardlist.pop())
            drawcounter += 1
            
        