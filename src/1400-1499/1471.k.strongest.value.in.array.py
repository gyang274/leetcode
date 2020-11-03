from typing import List

class Solution:
  def getStrongest(self, arr: List[int], k: int) -> List[int]:
    m = sorted(arr)[(len(arr) - 1) // 2]
    return [-x for _, x in sorted((-abs(x - m), -x) for x in arr)[:k]]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([-7,22,17,3], 2),
    ([6,7,11,7,6,8], 3),
    ([6,7,11,7,6,8], 5),
  ]
  rslts = [solver.getStrongest(arr, k) for arr, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
