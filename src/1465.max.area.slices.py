from typing import List

class Solution:
  def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
    # cuts on horizontal and vertical
    ch, cv = sorted([0] + horizontalCuts + [h]), sorted([0] + verticalCuts + [w])
    # slice on horizontal and vertical
    sh, sv = [ch[i + 1] - ch[i] for i in range(len(ch) - 1)], [cv[i + 1] - cv[i] for i in range(len(cv) - 1)]
    # max area
    return max(sh) * max(sv) % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (5, 4, [1,2,4], [2,3]),
  ]
  rslts = [solver.maxArea(h, w, horizontalCuts, verticalCuts) for h, w, horizontalCuts, verticalCuts in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
