
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
    def four_in_a_row(n):
      for c in self._cards[1:]:
        if c.n != n + 1:
          return False
        n += 1
      return True
  
    return (four_in_a_row(self._cards[0].n) 
      or (self._cards[0].n == 1 and four_in_a_row(9)))
  
  def is_straight_flush(self):
    return self.is_straight() and self.is_flush()

  def is_royal_flush(self):
    return self.is_straight_flush() and self._cards[0].n == 1


  def is_pair(self):
    c = 0
    for x in self._cards[1:]:
      f = self._cards[c].n
      if x.n == f:
        return True
      else:
        c += 1
    return False

  def is_3_of_a_kind():
    return False
 
  def is_full_house():
    return False

  def is_4_of_a_kind():
    return False

  def is_two_pair(self):
    r = 0
    c = 0
    for x in self._cards[1:]:
      f = self._cards[c].n
      print(f)
      print(x.n)
      if x.n == f:
        r += 1
        c += 1
        print(r)
        if r == 2: 
          return True
      else:
        c += 1
        print(c)
    return False


  
   
        
  
  

      
  def __str__(self):
    return ", ".join([str(x) for x in self._cards])