from typing import List
from collections import Counter

class Solution:
  def threeSumMulti(self, A: List[int], target: int) -> int:
    """O(N + M^2), M: num of unique values in A.
    """
    c1, c2, c3, d = 0, 0, 0, Counter(A)
    for x in d:
      if x + x + x == target:
        c1 += (d[x] * (d[x] - 1) * (d[x] - 2)) // 6
      s, t = set(), target - x
      for y in d:
        if not x == y:
          if y + y == t:
            c2 += d[x] * (d[y] * (d[y] - 1)) // 2
          elif t - y != x and t - y in s:
            c3 += d[x] * d[y] * d[t - y]
        s.add(y)
    return (c1 + c2 + c3 // 3) % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,1,2,2,2], 5),
    ([1,1,2,2,3,3,4,4,5,5], 8),
  ]
  rslts = [solver.threeSumMulti(A, target) for A, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
