from typing import List

class Solution:
  def replaceElements(self, arr: List[int]) -> List[int]:
    x = -1
    for i in range(len(arr) - 1, -1, -1):
      arr[i], x = x, max(arr[i], x)
    return arr

from itertools import accumulate

class Solution:
  def replaceElements(self, arr: List[int]) -> List[int]:
    return list(reversed(list(accumulate(reversed(arr), max, initial = -1))[:-1]))