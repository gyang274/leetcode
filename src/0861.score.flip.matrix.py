from typing import List

class Solution:
  def matrixScore(self, A: List[List[int]]) -> int:
    m, n, score = len(A), len(A[0]), 0
    # 1st col all 1s by flipping each row at the end
    score += m * (1 << (n - 1))
    # 2nd col more == 1st col than != 1st col by flipping col
    for j in range(1, n):
      count = sum(A[i][j] == A[i][0] for i in range(m))
      score += max(count, m - count) << (n - 1 - j)
    return score

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,0,1,1],[1,0,1,0],[1,1,0,0]],
  ]
  rslts = [solver.matrixScore(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
