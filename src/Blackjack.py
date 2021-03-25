import random

cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5,
         6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10,
         10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 1, 1, 1]

print("Lets play blackjack!\nI am the dealer, I will manage all the cards")
print("We will start now")

card = random.choice(cards)


def hit_me():
    return random.choice(cards)


def _pass():
    pass


def add():
    return card + random.choice(cards)


def game():
