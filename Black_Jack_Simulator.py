#Black_Jack Simulation with Python.
import os
import random
import pandas as pd

# 11 is jack worth 10 points
# 12 is queen worth 10 points
# 13 is king worth 10 points
# 14 is Ace worth 1 or 11 points


deck = [2,3,4,5,6,7,8,9,10,11,12,13,14,
        2,3,4,5,6,7,8,9,10,11,12,13,14,
        2,3,4,5,6,7,8,9,10,11,12,13,14,
        2,3,4,5,6,7,8,9,10,11,12,13,14]

def deal(deck):
    hand = []
    random.shuffle(deck)
    hand.append(deck.pop(1))
    hand.append(deck.pop(1))

    for n, i in enumerate(hand):
        if i == 11:
            hand[n] = 'J'
        if i == 12:
            hand[n] = 'Q'
        if i == 13:
            hand[n] = 'K'
        if i == 14:
            hand[n] = 'A'
    return(hand)

def count(hand):
    count = 0
    for i in hand:
        if i == "J" or i == "Q" or i == "K":
            count += 10
        elif i == 'A':
            if count >= 11:
                count += 1
            else:
                count += 10
        else:
            count += i
    return(count)

def hit(hand,deck):
    random.shuffle(deck)
    hand.append(deck.pop())
    return(hand)

""" attempting another method of dealing the cards or simply coding the game
in general"""

player_hand = deal(deck)
dealer_hand = deal(deck)

standing = False
first_hand = True

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    player_count = count(player_hand)
    dealer_count = count (dealer_hand)
    if standing:
        print("Dealer Cards: [{}], with a count of {}".format(dealer_hand,count(dealer_hand)))
    else:
        print("Dealer Cards: [{}], [?]".format(dealer_hand[0]))

    print("Player Cards: [{}], with a count of {}".format(player_hand,count(player_hand)))
    print(" ")


    if standing:
        if dealer_count > 21:
            print('Dealer Busted, you win!')
        elif player_count == dealer_count:
            print('Push, Nobody wins or loses')
        elif player_count > dealer_count:
            print('You beat the dealer, you win')
        else:
            print('your lose :( ')
        break

    if first_hand and player_count == 21:
        print('You win, Black_Jack')
        break

    if player_count > 21:
        print('You busted and lost :(')
        break

    question = input('What would you like to do [H]it, [S]tand, or [Q]uit ?'.lower())

    print('')
    if question == 'h':
        print(hit(player_hand,deck))
    elif question == 's':
        standing = True
        while count(dealer_hand) <=16:
            print(hit(dealer_hand,deck))
