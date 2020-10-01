from typing import List

class Solution:
  def checkIfExist(self, arr: List[int]) -> bool:
    seen = set()
    for x in arr:
      if (2 * x in seen) or ((x & 1) ^ 1 and x // 2 in seen):
        return True
      seen.add(x)
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [7,1,12,11],
    [7,1,14,11],
  ]
  rslts = [solver.checkIfExist(arr) for arr in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
