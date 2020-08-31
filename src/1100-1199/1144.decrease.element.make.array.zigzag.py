from typing import List

class Solution:
  def movesToMakeZigzag(self, nums: List[int]) -> int:
    # O(N), one pass, make nums[odd] smaller, or make nums[even] smaller
    nums = [float('inf')] + nums + [float('inf')]
    move = [0, 0]
    for i in range(1, len(nums) - 1):
      move[i & 1] += max(nums[i] - min(nums[i - 1], nums[i + 1]) + 1, 0)
    return min(move)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
    [2,7,10,9,8,9],
  ]
  rslts = [solver.movesToMakeZigzag(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
