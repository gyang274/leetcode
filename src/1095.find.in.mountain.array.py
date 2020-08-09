# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#  def get(self, index: int) -> int:
#  def length(self) -> int:

class Solution:
  def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
    # num of call to mountainArray API should <= O(sqrt(N))
    n = mountain_arr.length()
    # cache the call to mountain_arr: use cache or @lru_cache
    cache = {}
    def mA(i):
      # use cache or @lru_cache
      if i not in cache:
        cache[i] = mountain_arr.get(i)
      return cache[i]
    # O(2*logN) calls, binary search to find the peak in mountainArray, i s.t. A[i - 1] < A[i] > A[i + 1]
    l, r = 1, n - 2
    while l < r:
      m = l + (r - l) // 2
      if mA(m) > mA(m + 1):
        r = m
      else:
        l = m + 1
    # l is the peak
    p = l
    # O(logN) calls to search mountain peak left then right
    l, r = 0, p
    while l <= r:
      m = l + (r - l) // 2
      if mA(m) == target:
        return m
      elif mA(m) < target:
        l = m + 1
      else:
        r = m - 1
    l, r = p, n - 1
    while l <= r:
      m = l + (r - l) // 2
      if mA(m) == target:
        return m
      elif mA(m) > target:
        l = m + 1
      else:
        r = m - 1
    return -1