from functools import reduce

import operator

class Solution:
  def __init__(self):
    # memo: num of num with X unique digits
    self.memo = [0] * 11
    self.memo[1] = 9
    for i in range(2, 11):
      self.memo[i] = self.memo[i - 1] * (11 - i)
  def numDupDigitsAtMostN(self, N: int) -> int:
    S = str(N)
    n = len(S)
    if n == 1:
      return 0
    # count num of num with < n unique digits
    count = sum(self.memo[:n])
    # count num of num with = n unique digits
    seen = set()
    for i, x in enumerate(S):
      # num of num with unique digits and prefix S[:i] + z
      if i < n - 1:
        p = reduce(operator.mul, range(9 - i, 10 - n, -1))
      else:
        p = 1
      if i == 0:
        for z in range(1, int(x)):
          if str(z) not in seen:
            count += p
      else:
        for z in range(int(x)):
          if str(z) not in seen:
            count += p
      if x in seen:
        break
      seen.add(x)
    if len(seen) == n:
      count += 1
    return N - count

class Solution:
  def numDupDigitsAtMostN(self, N: int) -> int:
    S = list(map(int, str(N + 1)))
    count, n = 0, len(S)
    # A: m digits, n positions
    def A(m, n):
      return 1 if n == 0 else A(m, n - 1) * (m - n + 1)
    # count init with num of num with < n digits
    for i in range(1, n): 
      # no leading 0
      count += 9 * A(9, i - 1)
    # count the num of num with = n digits and <= N, along the prefix of S
    seen = set()
    for i, x in enumerate(S):
      for y in range(0 if i else 1, x):
        if y not in seen:
          count += A(9 - i, n - i - 1)
      if x in seen:
        break
      seen.add(x)
    return N - count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    20, 23, 42, 100, 1000, 20714715, 10 ** 9,
  ]
  rslts = [solver.numDupDigitsAtMostN(N) for N in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
