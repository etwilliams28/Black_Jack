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

def dealer_rules(hand,deck):
    random.shuffle(deck)
    hand.append(deck.pop())
    return(hand)

def black_jack(player_hand, dealer_hand):
    if player_hand == 21:
        print("Congrats your just got BlackJack")
    elif dealer_hand == 21:
        print("That,sucks the dealer just got Blackjack, you lost bub")


def score(player_hand,dealer_hand):
    while count(player_hand) <=21 and count(player_hand) <=21:
        if count(player_hand) == 21:
            print('Congrats you won! you just got BlackJack')
        elif count(dealer_hand) == 21:
            print("You loose, the dealer just got BlackJack")
        elif count(player_hand) > 21:
            print("Oopps you busted")
        elif count(player_hand) > count(dealer_hand):
            print('Congrats you win, good for you')
        elif count(player_hand) < count(dealer_hand):
            print('You loose, dealers hand was closer to 21')

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


"""

player_hand = deal(deck)
dealer_hand = deal(deck)
print(player_hand)
print("looks like your have a total of :{} ".format(count(player_hand)))
print("...")
print(dealer_hand)
print("Looks like the dealer has a total of {}".format(count(dealer_hand)))

##(hit(player_hand,deck)) //This is commented out for now
question = 0
question = (input("Would you like to hit or stay or quit?".lower()))

while question != 'quit'
    if question == 'hit':
        if count(player_hand) < 21:
            player_hand = hit(player_hand,deck)
            if count(dealer_hand) < 17:
                dealer_hand = (hit(dealer_hand,deck))
                print("you now have {}, for a toal of {} in your hand".format(player_hand,count(player_hand)))
                print("the dealer has {}, for a toal of {} in his hand".format(dealer_hand,count(dealer_hand)))
                print(score(player_hand,dealer_hand))

    elif question == "stay":
        player_hand = player_hand
        if count(dealer_hand) < 17:
            dealer_hand = (hit(dealer_hand,deck))
            score(player_hand,dealer_hand)


while count(player_hand) <= 21:
    hit_or_stay = (input("Would you like to hit or stay? ".lower()))
    if hit_or_stay == "hit":
        player_hand = (hit(player_hand,deck))
        print("")
        print("your hand is: {}".format(player_hand))
        black_jack(player_hand,dealer_hand)
        print(" ")
        print("you now have a total of count of : {}".format(count(player_hand)))

    while count(dealer_hand) <= 16:
        dealer_hand = hit(dealer_hand,deck)
        print(" ")
        print("dealer hand is: {} for a total of {}".format(dealer_hand,count(dealer_hand)))
        print()
        continue
        black_jack(player_hand,dealer_hand)
        score(player_hand,dealer_hand)
        break

    else:
        print(" ")
        print("you have chosen to stay and your count remains at : {}".format(count(player_hand)))
        print(" ")
        print("the dealers hand is {}".format(count(dealer_hand)))
    break
score(player_hand,dealer_hand)


"""
