from typing import List


# class Solution:
#   """Solution (DFS) contains duplicate combinations, duplicate as a result of permutation."""
#   def combinationSumRecursive(self, rslts: List[List[int]], candidates: List[int], rslt: List[int], target: int) -> None:
#     print(candidates, target, rslt)
#     if target == 0:
#       rslts.append(rslt)
#     for x in candidates:
#       if target - x >= 0:
#         self.combinationSumRecursive(rslts, candidates, rslt + [x], target - x)
#   def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#     rslts = []
#     self.combinationSumRecursive(rslts, candidates, [], target)
#     return rslts

class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    rslts = [[] for _ in range(target + 1)]
    for x in candidates:
      for i in range(x, target + 1):
        if i == x:
          rslts[i].append([x])
        else:
          for r in rslts[i - x]:
            rslts[i].append(r + [x])
    return rslts[target]


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ([2, 3, 6, 7], 7),
    ([2, 3, 5], 8),
  ]
  rslts = [solver.combinationSum(candidates, target) for candidates, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")