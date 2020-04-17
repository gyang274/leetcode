from typing import List

import itertools

class Solution:
  def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    n = len(nums)
    if n == 0:
      return []
    m = len(nums[0])
    if m == 0:
      return[[]]
    if not r * c == n * m or r == n:
      return nums
    it = itertools.chain.from_iterable(nums)
    return [list(itertools.islice(it, 0, c)) for _ in range(r)]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[1,2],[3,4]], 4, 1),
  ]
  rslts = [solver.matrixReshape(nums, r, c) for nums, r, c in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")

