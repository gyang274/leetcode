from typing import List

class Solution:
  def buildArray(self, target: List[int], n: int) -> List[str]:
    ans, k = [], 0
    for i in range(1, target[-1] + 1):
      if i < target[k]:
        ans.extend(["Push", "Pop"])
      else:
        ans.append("Push")
        k += 1
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,5,8,23,42,85],
  ]
  rslts = [solver.buildArray(target, n) for target, n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
