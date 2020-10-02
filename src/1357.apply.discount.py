class Cashier:

  def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
    self.x = 0
    self.n = n
    self.d = 1.0 - discount / 100
    self.p = {x: y for x, y in zip(products, prices)}

  def getBill(self, product: List[int], amount: List[int]) -> float:
    self.x += 1
    v = sum(self.p[x] * z for x, z in zip(product, amount))
    if self.x == self.n:
      v *= self.d
      self.x = 0
    return v
