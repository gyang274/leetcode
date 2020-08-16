from typing import List

class Solution:
  def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
    # 4-corner way of thinking
    maxVal = 0
    for corner in [[10**6 + 1, 10**6 + 1], [-10**6 - 1, 10**6 + 1], [-10**6 - 1, -10**6 - 1], [10**6 + 1, -10**6 - 1]]:
      distances = [abs(corner[0] - arr1[i]) + abs(corner[1] - arr2[i]) + i for i in range(len(arr1))]
      maxVal = max(maxVal, max(distances) - min(distances))
    return maxVal

class Solution:
  def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
    # 4-directions way of thinking
    maxVal = 0
    for x, y in [[1, 1], [1, -1], [-1, -1], [-1, 1]]:
      distances = [x * arr1[i] + y * arr2[i] + i for i in range(len(arr1))]
      maxVal = max(maxVal, max(distances) - min(distances))
    return maxVal

class Solution:
  def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
    # O(4N)
    ans, n = 0, len(arr1)
    for p, q in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
      smallest = p * arr1[0] + q * arr2[0] + 0
      for i in range(n):
        cur = p * arr1[i] + q * arr2[i] + i
        ans = max(ans, cur - smallest)
        smallest = min(smallest, cur)
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,3,4], [-1,4,5,6]),
  ]
  rslts = [solver.maxAbsValExpr(arr1, arr2) for arr1, arr2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
