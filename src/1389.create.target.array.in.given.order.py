from typing import List

class Solution:
  def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
    ans = []
    for i, x in zip(index, nums):
      ans.insert(i, x)
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1], [0]),
    ([0,1,2,3,4], [0,1,2,2,1]),
    ([1,2,3,4,0], [0,1,2,3,0]),
  ]
  rslts = [solver.createTargetArray(nums, index) for nums, index in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
