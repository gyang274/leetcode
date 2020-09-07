"""
This is the custom function interface.
You should not implement it, or speculate about its implementation
class CustomFunction:
  # Returns f(x, y) for any given positive integers x and y.
  # Note that f(x, y) is increasing with respect to both x and y.
  # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
  def f(self, x, y):
"""

class Solution:
  def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
    # It's guaranteed that the solutions of f(x, y) == z will be on the range 1 <= x, y <= 1000
    # It's also guaranteed that f(x, y) will fit in 32 bit signed integer if 1 <= x, y <= 1000, and 1 <= z <= 100.
    # 2D binary search, Q1274.
    ans, queue = set(), [((1, 1), (1000, 1000))]
    while queue:
      pBL, pTR = queue.pop()
      if pBL == pTR:
        if customfunction.f(*pBL) == z:
          ans.add(pBL)
      elif pBL[0] == pTR[0]:
        # split on y-axis
        m = pBL[1] + (pTR[1] - pBL[1]) // 2
        fxy = customfunction.f(pBL[0], m)
        if fxy == z:
          ans.add((pBL[0], m))
        elif fxy < z:
          queue.append(((pBL[0], m + 1), pTR))
        else:
          queue.append((pBL, (pBL[0], m - 1)))
      else:
        # split on x-axis
        m = pBL[0] + (pTR[0] - pBL[0]) // 2
        if customfunction.f(*pBL) <= z <= customfunction.f(m + 0, pTR[1]):
          queue.append((pBL, (m + 0, pTR[1])))
        if customfunction.f(m + 1, pBL[1]) <= z <= customfunction.f(*pTR):
          queue.append(((m + 1, pBL[1]), pTR))
    return ans

class Solution:
  def findSolution(self, customfunction, z):
    # note: y decrease globally, while x decrease, so amortized O(1), so overall TC: O(X + Y), SC: O(1)
    ans, y = [], 1000
    for x in range(1, 1001):
      while y > 1 and customfunction.f(x, y) > z:
        y -= 1
      if customfunction.f(x, y) == z:
        ans.append([x, y])
    return res
    