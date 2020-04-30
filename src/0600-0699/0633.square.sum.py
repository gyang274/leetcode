class Solution:
  def judgeSquareSum(self, c: int) -> bool:
    x = [i ** 2 for i in range(int(c ** 0.5) + 1)]
    y = set([])
    for v in x:
      y.add(v)
      if c - v in y:
        return True
    return False

class Solution:
  def judgeSquareSum(self, c: int) -> bool:
    # Fermat's Theorem: Any positive number n is expressible as a sum of two squares if and only if the prime 
    # factorization of n, every prime of the form (4k+3) occurs an even number of times.
    for i in range(2, int(c ** 0.5) + 1):
      count = 0
      if c % i == 0:
        while c % i == 0:
          count += 1
          c //= i
        if (i % 4 == 3 and not count % 2 == 0):
          return False
    return not c % 4 == 3
