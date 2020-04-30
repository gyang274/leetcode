class Solution:
  def __init__(self):
    self.memo = {}
    self.memo[1] = 0
  def minSteps(self, n: int) -> int:
    if n not in self.memo:
      # default copy once and paste n - 1 times
      self.memo[n] = n
      # if n % i == 0:
      #   get i, copy once and paste (n // i - 1) times
      #   get n // i, copy once and paste (i - 1) times
      for i in range(2, int(n ** 0.5) + 2):
        if n % i == 0:
          self.memo[n] = min(self.minSteps(i) + (n // i), self.minSteps(n // i) + i, self.memo[n])
    return self.memo[n]

class Solution(object):
  def minSteps(self, n):
    """prime factorization
    """
    cp, d = 0, 2
    while n > 1:
      while n % d == 0:
        cp += d
        n //= d
      d += 1
    return cp

if __name__ == '__main__':
  solver = Solution()
  cases = [
    1, 2, 3, 5, 8, 42, 85,
  ]
  rslts = [solver.minSteps(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
