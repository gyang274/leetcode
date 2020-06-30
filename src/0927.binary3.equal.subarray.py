from typing import List

class Solution:
  def threeEqualParts(self, A: List[int]) -> List[int]:
    n = len(A)
    # if possible, same num of 1s on each part, and 1s must be split equally,
    # say, [i1, j1], [i2, j2], [i3, j3], where i1, j1, i2, j2, i3, j3 all 1s,
    # and, num of 0s after j3 must be included for each segment length match.
    s = sum(A)
    if s % 3:
      return [-1, -1]
    s //= 3
    if not s:
      return [0, n - 1]
    # index of 1s
    o = [i for i in range(n) if A[i]]
    # split of 1s
    i1, i2, i3 = o[::s]
    j1, j2, j3 = o[(s - 1)::s]
    # check the equality
    if not A[i1:j1] == A[i2:j2] == A[i3:j3]:
      return [-1,-1]
    # append 0s
    k = n - j3
    j1 += k
    j2 += k
    return [j1 - 1, j2] if j1 <= i2 and j2 <= i3 else [-1, -1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,0,1,0,1],
    [1,1,0,1,1],
    [0,1,0,1,1,0,0,1,0,1,0,0,0,0,1,0,1,1,1,0]
  ]
  rslts = [solver.threeEqualParts(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
