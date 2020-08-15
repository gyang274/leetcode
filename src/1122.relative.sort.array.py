from typing import List

class Solution:
  def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    d = {x: i for i, x in enumerate(arr2)}
    return [x for i, x in sorted([(d.get(x, len(arr2)), x) for x in arr1])]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]),
  ]
  rslts = [solver.relativeSortArray(arr1, arr2) for arr1, arr2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
