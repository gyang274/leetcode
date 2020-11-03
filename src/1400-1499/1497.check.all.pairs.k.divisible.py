from typing import List
from collections import Counter

class Solution:
  def canArrange(self, nums: List[int], k: int) -> bool:
    # num of elements % k is x == num of elements % k is k - x
    # note special care on x == 0, and x == k / 2 if k is even
    d = Counter(map(lambda x: x % k, nums))
    if d[0] & 1:
      return False
    if (k & 1) ^ 1 and d[k // 2] & 1:
      return False
    for x in range(1, (k + 1) // 2):
      if not d[x] == d[k - x]:
        return False
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,3,4,5,6,7,8,9,10], 2),
    ([1,2,3,4,5,6,7,8,9,10], 3),
    ([1,2,3,4,5,6,7,8,9,10], 5),
  ]
  rslts = [solver.canArrange(nums, k) for nums, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
