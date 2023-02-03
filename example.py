# Tara Matuszek
# Dealing Cards
# Feb 2, 2023

"""
This program deals cards out to players from a deck.
The user can choose the number of players, and the number of cards dealt to the players.
The program will randomly deal and print the cards for a round, before asking if the user would like
to deal the next round or quit.  If there are not enough cards in the deck to deal to all players in
a round, the deck is reshuffled before dealing cards that round.
"""

# Setup
import random

def newDeal():
    '''
    This function is to reset to a full deck of cards.
    :return: a list containg the 52 cards in a standard deck as strings with the number follwed by suit icon
    '''
    deck = [
        "A♥️", "2♥️", "3♥️", "4♥️", "5♥️", "6♥️", "7♥️", "8♥️", "9♥️", "10♥️", "J♥️", "Q♥️", "K♥️",
        "A♥️", "2♠️️", "3♠️", "4♠️", "5♠️", "6♠️", "7♠️", "8♠️", "9♠️", "10♠️", "J♠️", "Q♠️", "K♠️",
        "A♦️", "2♦️", "3♦️", "4♦️", "5♦️", "6♦️", "7♦️", "8♦️", "9♦️", "10♦️", "J♦️", "Q♦️", "K♦️",
        "A♣️", "2♣️", "3♣️", "4♣️", "5♣️", "6♣️", "7♣️", "8♣️", "9♣️", "10♣️", "J♣️", "Q♣️", "K♣️",
    ]
    # ADD CODE HERE
    return deck


def dealHand(currentDeck, numCards = 5):
    '''
    This function will deal out a hand of cards for a play container.　for a person
    :param currentDeck: a list all cards currently left in the deck
    :param numCards: the number of cards to include in this players' hand
    :return:
        hand - a list containing the cards dealt
        currentDeck - an updated list containing all cards still left in the deck
    '''
    # ADD CODE HERE

for x in range (0,numCards):
    Removed = random.randint(0, len(deck))
    Remove = deck - Removed
    print(Remove)

def startGame(numPlayers = 2, numCards = 5):
    '''
    This function runs a card game, dealing out cards to players each round and
    reshuffling (use newDeal()) the deck if
    there aren't enough cards left for all players that round.
    It asks whether the user wants to continue after each round, and ends when they are done (the user chooses to end).
    :param numPlayers: the number of players in this card game
    :param numCards: the number of cards each player receives during each round
    '''
   # ADD CODE HERE
   # create playerDic = {p0: "", p1: "", p2...}
   # dealDeck = []
   # calculate how many cardsNeededtoDeal = numPlayer * numCards
   # create a keepPlaying = True
   # while keepPlaying == True:
       # if len(dealDeck) < cardsNeededtoDeal:
            # dealDeck = newDeal()
       # for playerNum in range(0, numPlayers+1):
           # for dealDeckNum in random.range():
                # for cardForPlayer in range(0, numCards+1):
                    # playerDic.upda
       # yn = input("Would you like to deal again?: ")
       # if yn == no, then keepPlaying = False
    #

# ADD CODE HERE (Should be only 3 lines)
numPlayers = int(input("How many players?: "))
numCards = int(input("How many cards do you want?"))
