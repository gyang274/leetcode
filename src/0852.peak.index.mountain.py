from typing import List

class Solution:
  def peakIndexInMountainArray(self, A: List[int]) -> int:
    return A.index(max(A))

class Solution(object):
  def peakIndexInMountainArray(self, A: List[int]) -> int:
    """O(logN): binary search
    """
    l, r = 0, len(A) - 1
    while l < r:
      m = l + (r - l) // 2
      if A[m] < A[m + 1]:
        l = m + 1
      else:
        r = m
    return l