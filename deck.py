from random import shuffle
from cards import Card
from hand import Hand

class Deck:

  def __init__(self):
    self.cards = []

    for suit in  ["Clubs","Diamonds","Hearts","Spades"]: 
      for n in range(1, 14):
        self.cards.append(Card(suit, n))
  
  def shuffle(self):
    shuffle(self.cards)

  def deal(self, hands = 2):
    return [Hand([self.cards[x] for x in range(h, hands * 5, hands)]) 
      for h in range(hands)]

    h1 = Hand([self.cards[x] for x in range(0, 9, 2)])
    h2 = Hand([self.cards[x] for x in range(1, 10, 2)])
    hands = (h1,h2)
    return hands