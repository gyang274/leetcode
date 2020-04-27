from typing import List

class Solution:
  def findNumberOfLIS(self, nums: List[int]) -> int:
    """O(N^2): dynamic programming, O(NlogN): segment tree.
    """
    if not nums:
      return 0
    n = len(nums)
    length, counts = [1] * n, [1] * n
    for j in range(n):
      for i in range(j):
        if nums[i] < nums[j]:
          if length[i] >= length[j]:
            length[j] = 1 + length[i]
            counts[j] = counts[i]
          elif length[i] == length[j] - 1:
            counts[j] += counts[i]
    longest = max(length)
    return sum([c for l, c in zip(length, counts) if l == longest])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,1,1,1,1],
    [2,3,5,4,7],
    [1,1,1,2,2,2,3,3,3],
  ]
  rslts = [solver.findNumberOfLIS(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
