from typing import List
from collections import Counter

class DSU:
  def __init__(self, reps: dict = {}):
    # representer
    self.reps = reps
  def add(self, x):
    self.reps[x] = x
  def find(self, x):
    if not x == self.reps[x]:
      self.reps[x] = self.find(self.reps[x])
    return self.reps[x]
  def union(self, x, y):
    self.reps[self.find(y)] = self.find(x)

class Solution:
  def largestComponentSize(self, A: List[int]) -> int:
    # dsu
    n, m = len(A), max(A)
    # primes as possible head
    p = [True] * (m + 1)
    p[0] = False
    # p[1] = True
    for i in range(2, int((m + 1) ** 0.5) + 1):
      if p[i]:
        j = 2 * i
        while j < m + 1:
          p[j] = False
          j += i
    primes = [i for i in range(m + 1) if p[i]]
    # dsu, key by prime factor of A[i]
    B = []
    for i, x in enumerate(A):
      ys = []
      if x in primes:
        ys.append(x)
      else:
        # option1: TLE
        # ys = []
        # for y in primes[1:]:
        #   if x % y == 0:
        #     while x % y == 0:
        #       x //= y
        #     ys.append(y)
        #   if x in primes:
        #     ys.append(x)
        #     break
        #   if y * y > x:
        #     break
        # option2: TLE
        # ys = []
        # i = 2
        # while primes[i] * primes[i] <= x:
        #   y = primes[i]
        #   if x % y == 0:
        #     while x % y == 0:
        #       x //= y
        #     ys.append(y)
        #   i += 1
        # if x > 1 or not ys:
        #   ys.append(x)
        # option3: why not TLE? 5x-10x faster than option1 and option2..
        ys, y = [], 2
        while y * y <= x:
          if x % y == 0:
            while x % y == 0:
              x //= y
            ys.append(y)
          y += 1
        if x > 1:
          ys.append(x)
      B.append(ys)
      A[i] = ys[0]
    # dsu, key by prime factor of A[i]
    dsu = DSU(reps={i: i for i in primes})
    for ys in B:
      for y in ys:
        dsu.union(ys[0], y)
    return max(Counter(map(dsu.find, A)).values())

class Solution:
  def largestComponentSize(self, A: List[int]) -> int:
    # A[i] -> unique prime factors
    B = []
    for i, x in enumerate(A):
      ys, y = [], 2
      while y * y <= x:
        if x % y == 0:
          while x % y == 0:
            x //= y
          ys.append(y)
        y += 1
      if x > 1 or not ys:
        ys.append(x)
      B.append(ys)
      A[i] = ys[0]
    # all primes
    primes = list({p for ys in B for p in ys})
    # dsu, key by prime factor of A[i]
    dsu = DSU(reps={i: i for i in primes})
    for ys in B:
      for y in ys:
        dsu.union(ys[0], y)
    return max(Counter(map(dsu.find, A)).values())

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [4,6,15,35],
    [20,50,9,63],
    [2,3,6,7,4,12,21,39],
    [1,2,3,19,57],
  ]
  rslts = [solver.largestComponentSize(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: | solution: {rs}")
