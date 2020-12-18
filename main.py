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
assert straight_flush.is_flush()
assert straight_flush.is_straight()
assert straight_flush.is_straight_flush()

royal_flush = Hand([Card("Spades", x) for x in range(10,14)]+[Card("Spades",1)])
assert royal_flush.is_straight()
assert royal_flush.is_royal_flush()

not_flush = Hand([Card("Spades", x) for x in range(1, 5)]+[Card("Hearts", 1)])
assert not(not_flush.is_flush())
assert not(not_flush.is_straight())
assert not not_flush.is_straight_flush()
assert not not_flush.is_royal_flush()

pair = Hand([Card(s, 8) for s in ["Hearts","Clubs"]]+[Card("Spades",x) for x in range(1,4)])
print(pair)
assert pair.is_pair()

three = Hand([Card(s, 8) for s in ["Hearts","Clubs","Diamonds"]]+[Card("Spades",x) for x in range(1,3)])
print(three)

four = Hand([Card(s, 8) for s in ["Hearts","Clubs","Diamonds","Spades"]]+[Card("Spades",x) for x in range(1,2)])
print(four)

two_pair = Hand([Card(s, 8) for s in ["Hearts","Clubs"]]+[Card(s, 9) for s in ["Hears","Clubs"]]+[Card("Spades",1)])
print(two_pair)
assert two_pair.is_two_pair()

full_house = Hand([Card(s, 8) for s in ["Hearts","Clubs"]]+[Card(s, 9) for s in ["Hearts","Clubs","Diamonds"]])
print(full_house)
