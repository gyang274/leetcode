from typing import List

class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    """Key: dynamic programming by keeping two status, current max and current min.
      memoryless so day i requires day i - 1 only, so dynamic programing -> status machine.
    """
    if len(nums) == 0: return 0
    xmax, xmin, omax = nums[0], nums[0], nums[0]
    for x in nums[1:]:
      xmax, xmin = max(xmax * x, xmin * x, x), min(xmax * x, xmin * x, x)
      omax = max(omax, xmax)
    return omax

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [],
    [2],
    [-2],
    [-2,0,-1],
    [2,3,-2,4],
    [2,3,-2,4,-6,8,-2,3,4,4,2],
  ]
  rslts = [solver.maxProduct(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")