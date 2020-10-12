from typing import List

class Solution:
  def minTaps(self, n: int, ranges: List[int]) -> int:
    r = [(max(0, i - x), min(i + x, n)) for i, x in enumerate(ranges)]
    r.sort(key=lambda x: (x[1], -x[0]))
    stack = []
    for s, e in r:
      while (stack and stack[-1][0] >= s) or (len(stack) > 1 and stack[-2][1] >= s):
        stack.pop()
      stack.append((s, e))
    x = 0
    for s, e in stack:
      if x >= s:
        x = e
      else:
        return -1
    return len(stack)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (3, [0,0,0,0]),
    (5, [3,4,1,1,0,0]),
    (7, [1,2,1,0,2,1,0,1]),
    (8, [4,0,0,0,0,0,0,0,4]),
    (8, [4,0,0,0,4,0,0,0,4]),
    (9, [0,5,0,3,3,3,1,4,0,4]),
    (17, [0,3,3,2,2,4,2,1,5,1,0,1,2,3,0,3,1,1]),
  ]
  rslts = [solver.minTaps(n, ranges) for n, ranges in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
