from typing import List


class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    m = len(matrix)
    if m == 0:
      return []
    n = len(matrix[0])
    il, ir, jl, jr = 0, m - 1, 0, n - 1
    x = []
    while il <= ir and jl <= jr:
      # print(f"{il=}, {ir=}, {jl=}, {jr=}")
      for j in range(jl, jr + 1):
        x.append(matrix[il][j])
      for i in range(il + 1, ir + 1):
        x.append(matrix[i][jr])
      if ir > il:
        for j in range(jr - 1, jl - 1, -1):
          x.append(matrix[ir][j])
      if jr > jl:
        for i in range(ir - 1, il, -1):
          x.append(matrix[i][jl])
      il += 1
      ir -= 1
      jl += 1
      jr -= 1
    return x


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    # [
    #   [ 1, 2, 3 ],
    #   [ 4, 5, 6 ],
    #   [ 7, 8, 9 ],
    # ],
    # [
    #   [1, 2, 3, 4],
    #   [5, 6, 7, 8],
    #   [9,10,11,12],
    # ],
    [
      [ 1, 2, 3],
      [ 4, 5, 6],
      [ 7, 8, 9],
      [10,11,12],
      [13,14,15],
    ],
    
  ]
  rslts = [solver.spiralOrder(matrix) for matrix in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")