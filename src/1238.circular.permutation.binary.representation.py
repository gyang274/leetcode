from typing import List

class Solution:
  def circularPermutation(self, n: int, start: int) -> List[int]:
    """Mirror Exender, Q0089.
    n = 0:
      [0]
    n = 1:
      [0]
      [1]
    n = 2:
      [0, 0]--+
      [0, 1]--+--+
      ------last position flipped [0, 1]->[1,0]
      [1, 1]--+--+
      [1, 0]--+
    n = 3:
      [0, 0, 0]--+
      [0, 0, 1]--+--+
        ------last position flipped
      [0, 1, 1]--+--+
      [0, 1, 0]--+
      ========last 2 positions flipped [(0,0), (0,1), (1,1), (1,0)] -> [(1,0), (1,1), (0,1), (0,0)]
      [1, 1, 0]--+
      [1, 1, 1]--+--+
        ------last position flipped
      [1, 0, 1]--+--+
      [1, 0, 0]--+
    """
    ans = [0]
    for i in range(n):
      ans += [z + (1 << i) for z in reversed(ans)]
    # update:
    #  O(logN) instead of O(N) to get the position of start directly in mirror extender.
    # for i, x in enumerate(ans):
    #   if x == start:
    #     return ans[i:] + ans[:i]
    pos, k = 0, 0
    while start:
      if start & 1:
        # flip
        pos = (1 << (k + 1)) - 1 - pos
      start >>= 1
      k += 1
    return ans[pos:] + ans[:pos]

class Solution:
  def circularPermutation(self, n: int, start: int) -> List[int]:
    # gray code
    return [start ^ (i ^ (i >> 1)) for i in range(1 << n)]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (1, 0),
    (2, 3),
    (3, 5),
    (5, 8),
    (8, 42),
  ]
  rslts = [solver.circularPermutation(n, start) for n, start in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")