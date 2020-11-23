from typing import List

class Solution:
  def numOfSubarrays(self, nums: List[int]) -> int:
    # se, so: total num of subarray sum is odd or even
    # o, e: num of subarray sum is odd or even using the current index as last
    so, se, o, e = 0, 0, 0, 0
    for x in nums:
      if x & 1:
        o, e = e + 1, o
      else:
        o, e = o, e + 1
      so += o
      se += e
    return so % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [0],
    [1],
    [0,0,1,1],
    [1,2,3,4,5,6,7],
  ]
  rslts = [solver.numOfSubarrays(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
