class StockSpanner:

  def __init__(self):
    self.span = []

  def next(self, price: int) -> int:
    days = 1
    while self.span and price >= self.span[-1][0]:
      days += self.span.pop()[1]
    self.span.append((price, days))
    return days