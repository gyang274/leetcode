from typing import List

class Solution:
  def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
    arr.sort()
    ans, mad = [], float('inf')
    for i in range(1, len(arr)):
      d = arr[i] - arr[i - 1]
      if d <= mad:
        if d < mad:
          ans, mad = [], d
        ans.append([arr[i - 1], arr[i]])
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
  ]
  rslts = [solver.minimumAbsDifference(arr) for arr in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
