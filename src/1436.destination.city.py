from typing import List

class Solution:
  def destCity(self, paths: List[List[str]]) -> str:
    x, y = zip(*paths)
    return (set(y) - set(x)).pop()

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [["A","Z"]],
    [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]],
  ]
  rslts = [solver.destCity(paths) for paths in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
