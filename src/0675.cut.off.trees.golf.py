from typing import List

class Solution:
  def cutOffTree(self, forest: List[List[int]]) -> int:
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [
      [1,2,3],
      [0,0,4],
      [7,6,5],
    ],
    [
      [1,2,3],
      [0,0,0],
      [7,6,5],
    ],
  ]
  rslts = [solver.cutOffTree(forest) for forest in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
