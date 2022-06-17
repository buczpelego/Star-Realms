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
    
    def change_location(self, current_location, destination):
        index = current_location.cardlist.index(self)
        destination.cardlist.append(current_location.cardlist.pop(index))
        return
    
class Area:
    def __init__(self, name):
        self.name = name
        self.cardlist = []
        
    def __repr__(self):
        presentation = {"Index" : [i + 1 for i in range(len(self.cardlist))],
                        "Card Name" : [card.name for card in self.cardlist],
                        'Color' : [card.color for card in self.cardlist],
                        'Damage' : [card.damage for card in self.cardlist],
                        'Gold' : [card.gold for card in self.cardlist],
                        'Regen' : [card.regen for card in self.cardlist],
                        'Cost' : [card.cost for card in self.cardlist]}
        presentation = pandas.DataFrame(presentation)
        presentation = tabulate(presentation, headers = 'keys', tablefmt='psql', showindex=False)
        print(self.name.upper())
        return presentation
        
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.gold = 0
        self.damage = 0
        self.starting_deck = []
        self.scout1 = GameCard("Scout", 'white', 0, 0, 1, 0)
        self.scout2 = GameCard("Scout", 'white', 0, 0, 1, 0)
        self.scout3 = GameCard("Scout", 'white', 0, 0, 1, 0)        
        self.scout4 = GameCard("Scout", 'white', 0, 0, 1, 0)
        self.scout5 = GameCard("Scout", 'white', 0, 0, 1, 0)
        self.scout6 = GameCard("Scout", 'white', 0, 0, 1, 0)
        self.scout7 = GameCard("Scout", 'white', 0, 0, 1, 0)
        self.scout8 = GameCard("Scout", 'white', 0, 0, 1, 0)
        self.viper1 = GameCard("Viper", 'white', 0, 1, 0, 0)
        self.viper2 = GameCard("Viper", 'white', 0, 1, 0, 0)
        self.starting_deck.extend([self.scout1, self.scout2, self.scout3, self.scout4, self.scout5, self.scout6, self.scout7, self.scout8, self.viper1, self.viper2])
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
            

        
