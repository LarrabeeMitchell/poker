
class Hand:

  def __init__(self, cards):
    self._cards = cards
    self._cards.sort()
  
  def is_flush(self):
    s = self._cards[0].s
    for c in self._cards[1:]:
      if c.s != s:
        return False 
    return True
  
  def is_straight(self):
    n = self._cards[0].n
    for c in self._cards[1:]:
      if c.n != n + 1:
        return False
      n += 1
    return True
  
  def is_straight_flush(self):
    if self.is_straight() == True and self.is_flush() == True:
      return True
    return False


    

  def __str__(self):
    return ", ".join([str(x) for x in self._cards])