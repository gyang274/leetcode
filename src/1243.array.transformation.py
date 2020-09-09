from typing import List

class Solution:
  def transformArray(self, arr: List[int]) -> List[int]:
    for _ in range(100):
      arr = arr[:1] + [b + (a > b < c) - (a < b > c) for a, b, c in zip(arr[:-2], arr[1:-1], arr[2:])] + arr[-1:]
    return arr
        