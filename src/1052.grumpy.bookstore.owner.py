from typing import List

class Solution:
  def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
    # O(N)
    satisfied = [x * (1 - y) for x, y in zip(customers, grumpy)]
    xs, xc, n = sum(satisfied[:X]), sum(customers[:X]), len(customers)
    xd = xc - xs
    for i in range(X, n):
      xs += satisfied[i] - satisfied[i - X]
      xc += customers[i] - customers[i - X]
      xd = max(xd, xc - xs)
    return sum(satisfied) + xd

class Solution:
  def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
    # O(N), one pass
    n = len(customers)
    # satisfied and reverse of grumpy
    satisfied, revgrumpy, maxrevgrumpy = 0, 0, 0
    for i in range(n):
      satisfied += customers[i] * (1 - grumpy[i])
      revgrumpy += customers[i] * grumpy[i]
      if i > X - 1:
        revgrumpy -= customers[i - X] * grumpy[i - X]
      maxrevgrumpy = max(maxrevgrumpy, revgrumpy)
    return satisfied + maxrevgrumpy

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3),
  ]
  rslts = [solver.maxSatisfied(customers, grumpy, X) for customers, grumpy, X in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
