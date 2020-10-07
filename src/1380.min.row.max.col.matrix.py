from typing import List

class Solution:
  def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
    return set(map(min, matrix)) & set(map(max, zip(*matrix)))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,10,4,2],[9,3,8,7],[14,15,17,12]],
  ]
  rslts = [solver.luckyNumbers(matrix) for matrix in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
