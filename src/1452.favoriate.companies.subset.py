from typing import List

class Solution:
  def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
    s = [set(x) for x in favoriteCompanies]
    return [i for i, si in enumerate(s) if all(i == j or not si.issubset(sj) for j, sj in enumerate(s))]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]],
  ]
  rslts = [solver.peopleIndexes(favoriteCompanies) for favoriteCompanies in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
