from typing import List

class Solution:
  def findBestValue(self, arr: List[int], target: int) -> int:
    # O(NlogN), sort
    arr.sort(reverse=True)
    # O(N), one pass
    xmax = arr[0]
    while arr and target >= arr[-1] * len(arr):
      target -= arr.pop()
    if not arr:
      return xmax
    q, r = target // len(arr), target % len(arr)
    return q if r <= len(arr) - r else q + 1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,3,4,5], 10),
  ]
  rslts = [solver.findBestValue(arr, target) for arr, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
