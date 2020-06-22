from typing import List

class Solution:
  def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
    d, s, r, c, ans = 1, 1, r0, c0, [[r0, c0]]
    while len(ans) < R * C:
      for i in range(s):
        c += 1 * d
        if 0 <= r < R and 0 <= c < C:
          ans.append([r, c])
      for j in range(s):
        r += 1 * d
        if 0 <= r < R and 0 <= c < C:
          ans.append([r, c])
      d = -d
      s += 1
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (1, 4, 0, 0),
    (5, 8, 1, 4),
  ]
  rslts = [solver.spiralMatrixIII(R, C, r0, c0) for R, C, r0, c0 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")