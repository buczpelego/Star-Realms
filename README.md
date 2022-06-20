# Star-Realms
This is my implementation of basic mechanics for boardgame called "Star Realms".
I created this project for Codecademy course purposes with idea for further upgrading it when my knowledge allows.

In, shourtcut:
It's a cardgame, where 2 player (1 user and 1 cpu) deal with each other in space combat using cards. Cards visualise different spaceships with different stats.
Both players start game with 50 health points and same basic deck. They will be using cards to buy new stronger ships from common "Market Area". They add new cards 
to their decks and can use them later to buy even more cards and deal more damage to enemy.

From backend perspective:
After launch "startgame.py", 
1. game uses "classobject.py" and creates cards that are saved in "cards.py". 
2. creates instances for Player1 and Cpu player in "maingamefile.py" (file where whole game proceeds)
3. creating Player instances creates for them individual areas - Deck Area (from where player pulls cards to hand)
                                                               - Hand Area (where player holds his cards and play them on table to.....
                                                               - Play Area (where game counts basic stats lige gold and damage from played cards)
                                                               - Discard Area (where used cards land both with newly bougth cards)
4. creates common areas - Market Area (new more powerfull cards appear there)
                        - Market Deck Area (supply for Market Area)
                        - Explorer Area (Area where both players can buy Explorer Cards)
                        - Bin Area (Area where lands all cards destroyed by different card abilities - currently unavalible)

Player 1 starts with 5 cards on hand and can play them for free into his Play Area. Cards have two main stats: Gold - that allow to buy new cards from Market
and Damage - that deals damage to enemy player.
After playing cards from hand into Play Area, game sums up all Gold and Damage from played cards and shows Cards in Market. Player 1 is buying cards from Market. 
After each perchuase, new card goes into Player Discard Area and new card is beeing pulled from Market Deck into Market so there are always 5 cards avalible. 
After Market phase, all Damage from played cards hits enemy player, and cards in both Play Area and Hand Area (that havent been played), goes into discard. 
Than, player pulls up to 5 cards from deck into his hand for his next turn. If Deck is empty, Discard Area is beeing shuffled and all cards goes into Deck Area, 
so every perchuased card will sooner or later go into player hand. Playing card from hand is free, only cost in game apears when you have to buy card from market. 
During market phase, if there is a situation that none of avalible cards suits you you can buy Explorer Card from Explorer Deck. Explorers are cheap, slighty better
basic cards avalible in game.

After player turn, enemy CPU turn goes the same way. There is implemented some realy basic AI where CPU enemy always plays every card avalible in hand, buys most expensive
cards in Market that he can afford and deals damage to Player. 

