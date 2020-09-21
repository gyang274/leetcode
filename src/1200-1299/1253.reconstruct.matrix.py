from typing import List

class Solution:
  def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
    if upper + lower != sum(colsum):
      return []
    matrix = [[0] * len(colsum) for _ in range(2)]
    for i in range(len(colsum)):
      if colsum[i] == 2:
        if upper > 0 and lower > 0:
          matrix[0][i] = 1
          matrix[1][i] = 1
          upper -= 1
          lower -= 1
        else:
          return []
      elif colsum[i] == 1:
        if upper > lower:
          matrix[0][i] = 1
          upper -= 1
        else:
          matrix[1][i] = 1
          lower -= 1
    return matrix

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, 3, [1,3,0,1]),
    (5, 5, [2,1,2,0,1,0,1,2,0,1]),
    (9, 2, [0,1,2,0,0,0,0,0,2,1,2,1,2]),
  ]
  rslts = [solver.reconstructMatrix(upper, lower, colsum) for upper, lower, colsum in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
