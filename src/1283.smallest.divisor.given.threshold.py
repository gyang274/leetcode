from typing import List

class Solution:
  def smallestDivisor(self, nums: List[int], threshold: int) -> int:
    # binary search
    hash = lambda k: sum(map(lambda x: (x - 1) // k + 1, nums))
    l, r = 1, max(nums)
    while l < r:
      m = l + (r - l) // 2
      if hash(m) <= threshold:
        r = m
      else:
        l = m + 1
    return l

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,3,1,1,4], 4),
  ]
  rslts = [solver.smallestDivisor(nums, threshold) for nums, threshold in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
