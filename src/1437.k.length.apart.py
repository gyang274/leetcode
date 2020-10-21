from typing import List

class Solution:
  def kLengthApart(self, nums: List[int], k: int) -> bool:
    i = float('-inf')
    for j, x in enumerate(nums):
      if x:
        if j - i <= k:
          return False
        i = j
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,0,0,1,0,0,0,1], 2),
    ([1,0,0,1,0,0,0,1], 3),
  ]
  rslts = [solver.kLengthApart(nums, k) for nums, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
