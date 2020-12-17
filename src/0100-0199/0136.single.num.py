from typing import List

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    """Binary xor `^` operator.
    """
    x = 0
    for y in nums:
      x ^= y
    return x

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [0],
    [2,1,2],
    [1,2,4,1,2]
  ]
  rslts = [solver.singleNumber(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  