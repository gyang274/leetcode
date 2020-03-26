from typing import List

class Solution:
  def numberOfArithmeticSlices(self, A: List[int]) -> int:
    return 0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1, 2, 3, 5, 8, 11, 14, 17, 22, 42, 43, 46, 49, 52, 55, 58, ],
  ]
  rslts = [solver.numberOfArithmeticSlices(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")