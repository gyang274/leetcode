from typing import List

class Solution:
  def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
    # binary search, O(NlogS)
    # N, S = len(sweetness), sum(sweetness)
    l, r = min(sweetness), sum(sweetness)
    # key, O(N) each iteration, is sweetness x achievable or not
    def isSweetnessOk(x):
      count, sweet = 0, 0
      for s in sweetness:
        sweet += s
        if sweet >= x:
          count += 1
          sweet = 0
      return count > K
    # O(logS) searches, O(N) at each iteration
    while l < r:
      m = r - (r - l) // 2
      if isSweetnessOk(m):
        l = m
      else:
        r = m - 1
    return l

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,2,1,2,2,1,2,2], 2),
    ([1,2,3,4,5,6,7,8,9], 2),
    ([1,2,3,4,5,6,7,8,9], 3),
    ([1,2,3,4,5,6,7,8,9], 5),
    ([1,2,3,4,5,6,7,8,9], 8),
  ]
  rslts = [solver.maximizeSweetness(sweetness, K) for sweetness, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
