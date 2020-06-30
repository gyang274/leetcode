from typing import List
from collections import Counter
from itertools import accumulate

class Solution:
  def numSubarraysWithSum(self, A: List[int], S: int) -> int:
    # index of 1s
    ones = [i for i, x in enumerate(A) if x]
    # segment length, e.g., num of 0s between 1s
    zero = [j - i - 1 for i, j in zip([-1] + ones, ones + [len(A)])]
    # count
    if S == 0:
      return sum(z * (z + 1) // 2 for z in zero)
    n = len(ones)
    if S > n:
      return 0
    return sum((zero[i] + 1) * (zero[i + S] + 1) for i in range(n + 1 - S))

class Solution:
  def numSubarraysWithSum(self, A: List[int], S: int) -> int:
    # prefix sum, let B = accumulate(A, initial=0), B[j] - B[i] = S if B[j] - S = B[i] for some i < j.
    ans, count = 0, Counter()
    for s in accumulate(A, initial=0):
      # s is the B[j], count[s - S] is the num of B[i] = B[j] - S seen with i < j.
      ans += count[s - S]
      count[s] += 1
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,0,1,0,1], 0),
    ([1,0,1,0,1], 1),
    ([1,0,1,0,1], 2),
    ([1,0,1,0,1], 3),
    ([1,0,1,0,1], 4),
  ]
  rslts = [solver.numSubarraysWithSum(A, S) for A, S in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
