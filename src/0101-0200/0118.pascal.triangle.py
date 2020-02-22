from typing import List

class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    x = []
    for i in range(numRows):
      x.append([1] * (i + 1))
      for j in range(1, i):
        x[i][j] = x[i - 1][j - 1] + x[i - 1][j]
    return x

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    0,
    1,
    2,
    3,
    5,
    8,
  ]
  rslts = [solver.generate(numRows) for numRows in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  