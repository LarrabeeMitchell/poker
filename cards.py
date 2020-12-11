class Card:
  def __init__(self, s, n):
    self.s = s
    self.n = n

  def number(self):
    return {1:"Ace", 11:"Jack", 12:"Queen", 13:"King"}.get(
      self.n,
      str(self.n)
      )

  def __str__(self):
    return f"{self.number()} of {self.s}"