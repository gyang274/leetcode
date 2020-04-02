from typing import List

class Solution:
  def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    # n1: current consecutive ones
    # n2: current consecutive ones with flip of most recent 0
    n1, n2, nX = 0, 0, 0
    for x in nums:
      if x == 0:
        n2 = n1 + 1
        n1 = 0
      else:
        n2 += 1
        n1 += 1
      nX = max(nX, n2)
    return nX

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [1,0,1,1],
    [1,0,1,1,0,1,0,0],
  ]
  rslts = [solver.findMaxConsecutiveOnes(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
