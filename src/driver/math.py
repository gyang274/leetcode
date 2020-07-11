class Solution:

  def getGCD(self, x: int, y: int) -> int:
    while y:
      x, y = y, x % y
    return x  
  
  def getLCM(self, x: int, y: int) -> int:
    return x * y // self.getGCD(x, y)
  
  def isPrime(self, x: int) -> bool:
    return x > 1 and all(x % d for d in range(2, int(x ** 0.5) + 1))
  
  def triangleArea(self, x1, y1, x2, y2, x3, y3) -> float:
    #       |     |- x1 y1 1 -| |
    # 1/2 * | det |  x2 y2 1  | |
    #       |     |_ x3 y3 1 _| |
    return abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
