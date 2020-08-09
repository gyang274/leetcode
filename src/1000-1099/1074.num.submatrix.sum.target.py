from typing import List
from collections import defaultdict
from itertools import accumulate

class Solution:
  def numSubvectorSumTarget(self, nums: List[int], target: int) -> int:
    # solver over 1D, O(N)
    d, count = defaultdict(lambda: 0), 0
    # prefix sum over nums
    d[0] = 1
    for x in accumulate(nums):
      count += d[x - target]
      d[x] += 1
    return count
  def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
    # O(min((R^2)*C, R*(C^2)))
    m, n = len(matrix), len(matrix[0])
    if m > n:
      m, n, matrix = n, m, list(map(list, zip(*matrix)))
    # prefix sum over cols
    for i in range(1, m):
      for j in range(n):
        matrix[i][j] += matrix[i - 1][j]
    # count
    count = 0
    # 1D over each rows
    for i in range(m):
      count += self.numSubvectorSumTarget(matrix[i], target)
    # 1D over each pair of rows
    for j in range(m):
      for i in range(j):
        count += self.numSubvectorSumTarget([y - x for x, y in zip(matrix[i], matrix[j])], target)
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[1,-1],[-1,1]], 0),
    ([[0,1,0],[1,1,1],[0,1,0]], 0),
    ([[0,0,0,1,1],[1,1,1,1,1],[0,1,0,0,0],[0,1,0,0,0],[1,1,1,1,0],[1,1,1,0,1]], 0),
  ]
  rslts = [solver.numSubmatrixSumTarget(matrix, target) for matrix, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
