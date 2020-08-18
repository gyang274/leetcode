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

  def countDigitK(self, n: int, k: int) -> int:
    # count num of digit k appearance on all positive integer x, 1 <= x <= n.
    count, m = 0, 1
    while n > m - 1:
      q, r = n // (10 * m), n % (10 * m)
      if k == 0:
        count += (q * m) if r >= m else ((q - 1) * m + r + 1)
      else:
        count += q * m + min(max(0, r - m * k + 1), m)
      m *= 10
    return count

  def catalan(self, n):
    # catalan number: C_{0} = 1, C_{n+1} = \sum_{i=0}^{n} C_{i} * C_{n-i}, n > 0
    # C_{n} = choose(2n, n) - choose(2n, n+1) = choose(2n, n) / (n + 1), n > 0
    x = 1
    for i in range(1, n // 2 + 1):
      x *= n - i + 1
      x //= i
    x //= (n // 2 + 1)
    return x