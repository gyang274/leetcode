from typing import List

class Solution:
  def totalFruit(self, tree: List[int]) -> int:
    x1, x2, s1, s2, curr, cmax = None, None, 0, 0, 0, 0
    for i, x in enumerate(tree):
      if x == x2:
        pass  
      elif x == x1:
        x1, x2 = x2, x
        s1, s2 = s2, i
      else:
        x1, x2 = x2, x
        s1, s2 = s2, i
        curr = i - s1
      curr += 1
      cmax = max(cmax, curr)
    return cmax

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [0],
    [0,1,2,1,1,3,3,3,4,3],
  ]
  rslts = [solver.totalFruit(tree) for tree in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
