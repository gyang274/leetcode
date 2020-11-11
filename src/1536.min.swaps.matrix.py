from typing import List

class Solution:
  def minSwaps(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    # summarize each row to last index of 1s
    row = [0] * m
    for i in range(m):
      row[i] = next((j for j in reversed(range(n)) if grid[i][j]), 0)
    # like bubble sort
    # fill each target row sequentially, s.t. row[i] = x <= i
    ans = 0
    for i in range(m):
      for k, x in enumerate(row):
        if x <= i:
          # k-th row pop to front with k moves
          ans += k
          row.pop(k)
          break
      else:
        return -1
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,0,0],[1,1,0],[1,1,1]],
    [[0,0,1],[1,1,0],[1,0,0]],
    [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]],
  ]
  rslts = [solver.minSwaps(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
