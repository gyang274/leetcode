from typing import List

class Solution:
  def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
    n, count = len(arr), 0
    for i in range(n - m):
      count = (count + 1) if arr[i] == arr[i + m] else 0
      if count == m * (k - 1):
        return True
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,4,4,4,4], 1, 2),
    ([1,2,4,4,4,4], 2, 3),
  ]
  rslts = [solver.containsPattern(arr, m, k) for arr, m, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
