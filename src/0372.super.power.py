from typing import List
from collections import deque

class Solution:
  def __init__(self):
    self.m = 1337
  def divide2(self, b: List[int]) -> int:
    """calculate b // 2 in place, and return b % 2.
    """
    k = 0
    for i in range(len(b)):
      r = b[i] % 2
      b[i] = (k * 10 + b[i]) // 2
      k = r
    if len(b) > 1 and b[0] == 0:
      b.popleft()
    return r
  def superPow(self, a: int, b: List[int]) -> int:
    """O(logN), Q0050.
    """
    if len(b) == 0:
      return 1
    # make popleft O(1)
    b = deque(b)
    # double a's
    x, a = 1, a % self.m
    while not (len(b) == 1 and b[0] == 0):
      r = self.divide2(b)
      if r == 1:
        x *= a
        x %= self.m
      a *= a
      a %= self.m
    return x

class Solution:
  def __init__(self):
    self.m = 1337
  def superPow(self, a: int, b: List[int]) -> int:
    """O(log_{10}(N)), Q0050.
    """
    if len(b) == 0:
      return 1
    x, a = 1, a % self.m
    while b:
      r = b.pop()
      x *= a ** r
      x %= self.m
      a *= a ** 9
      a %= self.m
    return x

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (1142, [4,1,2,3,5,8,9,6,0,7]),
  ]
  rslts = [solver.superPow(a, b) for a, b in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")