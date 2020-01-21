from typing import List


class Solution:
  def combinationSum2Recursive(self, rslts, candidates, rslt, target):
    if target == 0:
      rslts.append(rslt)
    else:
      for i, x in enumerate(candidates):
        if i > 0 and candidates[i] == candidates[i - 1]:
          continue
        if target >= x:
          self.combinationSum2Recursive(rslts, candidates[(i+1):], rslt+[x], target-x)
  def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    rslts = []
    self.combinationSum2Recursive(rslts, candidates, [], target)
    return rslts


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ([4, 4, 2, 1, 4, 2, 2, 1, 3], 6),
    ([1, 1, 1, 1, 2, 3, 4, 5], 8),
    ([10, 1, 2, 7, 6, 1, 5], 8),
    ([2, 5, 2, 1, 2], 5),
  ]
  rslts = [solver.combinationSum2(candidates, target) for candidates, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")