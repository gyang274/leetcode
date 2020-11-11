from typing import List

class Solution:
  def countGoodTriplets(self, nums: List[int], x: int, y: int, z: int) -> int:
    n, count = len(nums), 0
    for i in range(n):
      for j in range(i + 1, n):
        if abs(nums[i] - nums[j]) <= x:
          for k in range(j + 1, n):
            if abs(nums[j] - nums[k]) <= y and abs(nums[i] - nums[k]) <= z:
              count += 1
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([3,2,1,4,7,2], 2, 3, 5),
  ]
  rslts = [solver.countGoodTriplets(nums, x, y, z) for nums, x, y, z in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
