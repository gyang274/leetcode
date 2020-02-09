from typing import List

class Solution:
  def getRow(self, rowIndex: int) -> List[int]:  
    x = [1] * (rowIndex + 1)
    for i in range(rowIndex + 1):
      for j in range(i - 1, 0, -1):
        x[j] = x[j] + x[j - 1]
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
  rslts = [solver.getRow(rowIndex) for rowIndex in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  