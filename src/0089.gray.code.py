from typing import List


class Solution:
  def grayCode(self, n: int) -> List[int]:
    """Mirror Exender.
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
    x = [0]
    for i in range(n):
      x += [z + (1 << i) for z in reversed(x)]
    return x


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    0,
    1,
    2,
    3,
    4,
    5, 
  ]
  rslts = [solver.grayCode(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")