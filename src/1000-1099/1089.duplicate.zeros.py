from typing import List
from collections import Counter

class Solution:
  def duplicateZeros(self, arr: List[int]) -> None:
    """Do not return anything, modify arr in-place instead.
    """
    n = len(arr)
    # move
    m = Counter(arr)[0]
    # make move
    for i in range(n - 1, -1, -1):
      if i + m < n:
        arr[i + m] = arr[i]
      if arr[i] == 0:
        m -= 1
        if i + m < n:
          arr[i + m] = arr[i]
    return None

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [1,0,2,3,0,4,5,0],
    [0,1,9,2,6,0,0,4,1,0],
  ]
  rslts = [solver.duplicateZeros(arr) for arr in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
