from cards import Card
from deck import Deck 
from hand import Hand

d = Deck()
d.shuffle()
h1, h2, h3 = d.deal(3)

c1 = Card("Hearts", 7)
c2 = Card("Hearts", 5)

assert c1 == c1
assert c1 != c2
assert c2 < c1
assert c1 > c2

straight_flush = Hand([Card("Spades", x) for x in range(1,6)])
assert(straight_flush.is_flush())
assert(straight_flush.is_straight())
assert straight_flush.is_straight_flush()
not_flush = Hand([Card("Spades", x) for x in range(1, 5)]+[Card("Hearts", 1)])
assert not(not_flush.is_flush())
assert not(not_flush.is_straight())
assert not not_flush.is_straight_flush()