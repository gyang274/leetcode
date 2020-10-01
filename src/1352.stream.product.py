class ProductOfNumbers:

  def __init__(self):
    self.x = [1]

  def add(self, num: int) -> None:
    if num == 0:
      self.x = [1]
    else:
      self.x.append(self.x[-1] * num)

  def getProduct(self, k: int) -> int:
    return 0 if k >= len(self.x) else self.x[-1] // self.x[-(k + 1)]
