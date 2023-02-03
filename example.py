# Tara Matuszek
# Dealing Cards
# Feb 2, 2023 -- NEW UPDATE

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
    :return: a list containing the 52 cards in a standard deck as strings with the number followed by suit icon
    '''
    deck = [
        "A♥️", "2♥️", "3♥️", "4♥️", "5♥️", "6♥️", "7♥️", "8♥️", "9♥️", "10♥️", "J♥️", "Q♥️", "K♥️",
        "A♥️", "2♠️️", "3♠️", "4♠️", "5♠️", "6♠️", "7♠️", "8♠️", "9♠️", "10♠️", "J♠️", "Q♠️", "K♠️",
        "A♦️", "2♦️", "3♦️", "4♦️", "5♦️", "6♦️", "7♦️", "8♦️", "9♦️", "10♦️", "J♦️", "Q♦️", "K♦️",
        "A♣️", "2♣️", "3♣️", "4♣️", "5♣️", "6♣️", "7♣️", "8♣️", "9♣️", "10♣️", "J♣️", "Q♣️", "K♣️",
    ]
    # return deck of cards
    num = random.randint(0, len(deck))
    print(deck[num] + "  " + str(num))


def dealHand(currentDeck, numCards = 5):
    '''
    This function will deal out a hand of cards for a player.
    :param currentDeck: a list containing all cards currently left in the deck
    :param numCards: the number of cards to include in this players' hand
    :return:
        hand - a list containing the cards dealt
        currentDeck - an updated list containing all cards still left in the deck
    '''
    # ADD CODE HERE


def startGame(numPlayers = 2, numCards = 5):
    '''
    This function runs a card game, dealing out cards to players each round and reshuffling the deck if
    there aren't enough cards left for all players that round.
    It asks whether the user wants to continue after each round, and ends when they are done.
    :param numPlayers: the number of players in this card game
    :param numCards: the number of cards each player receives during each round
    '''
   # deck for (0:51)
    def Reset(deck <= 51):
   input("Is the game over?y/n");
   while y,
       input("Does the deck have 52 cards?y/n");
        if n,
            deck = Reset







# ADD CODE HERE (Should be only 3 lines)