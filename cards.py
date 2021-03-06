import functools

@functools.total_ordering
class Card:
  def __init__(self, s, n):
    self.s = s
    self.n = n

  def number(self):
    return {1:"Ace", 11:"Jack", 12:"Queen", 13:"King"}.get(
            self.n,
      str(self.n)
      )

  def __eq__(self, other):
    return self.n == other.n

  def __lt__(self, other):
    return self.n < other.n

  def __str__(self):
    return f"{self.number()} of {self.s}"