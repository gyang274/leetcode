from typing import List

class Solution:
  def getWinner(self, nums: List[int], k: int) -> int:
    # TC: O(N), SC: O(1).
    n = len(nums)
    if k >= n:
      return max(nums)
    cur, win = nums[0], 0
    for i in range(1, n):
      if nums[i] > cur:
        cur, win = nums[i], 0
      win += 1
      if win == k:
        break
    return cur

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,1,4,5,3,7,6], 2),
  ]
  rslts = [solver.getWinner(nums, k) for nums, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
