from typing import List

from functools import lru_cache
from itertools import accumulate

class Solution:
  def mergeStones(self, stones: List[int], K: int) -> int:
    N = len(stones)
    if K > 2 and not N % (K - 1) == 1:
      return -1
    # prefix sum
    s = [0] + list(accumulate(stones))
    # dynamic programmin, divide and conquer
    @lru_cache(None)
    def dp(i, j):
      if (j - i) < K:
        return 0
      ans = min(dp(i, x) + dp(x, j) for x in range(i + 1, j, K - 1))
      if (j - i - 1) % (K - 1) == 0:
        ans += s[j] - s[i]
      return ans
    return dp(0, N)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,3,1,1,4], 3),
  ]
  rslts = [solver.mergeStones(stones, K) for stones, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
