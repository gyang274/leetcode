from typing import List

class Solution:
  def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
    return [x for d, j, i, x in sorted([(i + j, j, i, x) for i, r in enumerate(nums) for j, x in enumerate(r)])]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,2,3,4,5,6]],
    [[1,2,3],[4,5,6],[7,8,9]],
    [[1,2,3],[4],[5,6,7],[8],[9,10,11]],
    [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]],
  ]
  rslts = [solver.findDiagonalOrder(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
