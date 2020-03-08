from typing import List

class Solution:
  def _mergesort(self, nums):
    m = len(nums) // 2
    if m > 0:
      l, r = self._mergesort(nums[:m]), self._mergesort(nums[m:])
      # count the i, j s.t., l[i] > r[j] * 2, only need the first j from right in r since sorted
      j = 0
      for xl in l:
        while j < len(r) and xl > r[j] * 2:
          j += 1
        self.counter += j
      # merge sort, return the sorted l, r combined, so O(NlogN) overall
      for i in range(len(nums) - 1, -1, -1):
        if l and r:
          nums[i] = l.pop() if l[-1] > r[-1] else r.pop()
        elif l:
          nums[i] = l.pop()
        else:
          nums[i] = r.pop()
    return nums
  def reversePairs(self, nums: List[int]) -> int:
    """Q0315, Q0327, O(NlogN), divide and conquer, modified mergesort.
    """
    self.counter = 0
    self._mergesort(nums)
    return self.counter

class Solution:
  def _mergesort(self, nums):
    m = len(nums) // 2
    if m > 0:
      l, r = self._mergesort(nums[:m]), self._mergesort(nums[m:])
      # merge sort, return the sorted l, r combined, so O(NlogN) overall
      # count the i, j s.t., l[i] > r[j] * 2, only need the first j from right in r since sorted
      j, k, i = 0, 0, 0
      for xl in l:
        while j < len(r) and xl > r[j] * 2:
          j += 1
        self.counter += j
        while k < len(r) and xl > r[k]:
          nums[i] = r[k]
          k += 1
          i += 1
        nums[i] = xl
        i += 1
      if k < len(r):
        nums[i:] = r[k:]
    return nums
  def reversePairs(self, nums: List[int]) -> int:
    """Q0315, Q0327, O(NlogN), divide and conquer, modified mergesort.
    """
    self.counter = 0
    self._mergesort(nums)
    return self.counter

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [-5,-5],
    [1,3,2,3,1],
    [2,4,3,5,1],
  ]
  rslts = [solver.reversePairs(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")