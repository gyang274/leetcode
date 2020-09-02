from typing import List

class Solution:
  def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
    i1, i2, i3, n1, n2, n3 = 0, 0, 0, len(arr1), len(arr2), len(arr3)
    ans = []
    while i1 < n1 and i2 < n2 and i3 < n3:
      x1, x2, x3 = arr1[i1], arr2[i2], arr3[i3]
      if x1 == x2 == x3:
        ans.append(x1)
        i1 += 1
        i2 += 1
        i3 += 1
      else:
        if x1 <= min(x2, x3):
          i1 += 1
        if x2 <= min(x3, x1):
          i2 += 1
        if x3 <= min(x1, x2):
          i3 += 1
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,3,4,5], [1,2,5,7,9], [1,3,4,5,8]),
  ]
  rslts = [solver.arraysIntersection(arr1, arr2, arr3) for arr1, arr2, arr3 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
