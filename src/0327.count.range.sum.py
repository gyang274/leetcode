from typing import List

class Solution:
  def _mergesort(self, nums):
    m = len(nums) // 2
    if m > 0:
      l, r = self._mergesort(nums[:m]), self._mergesort(nums[m:])
      # only need between l, r, using two pointers j1 and j2 to bound r[j] - l[i] within [lower, upper]
      j1, j2 = 0, 0
      for xl in l:
        while j1 < len(r) and r[j1] - xl < self.lower:
          j1 += 1
        while j2 < len(r) and r[j2] - xl <= self.upper:
          j2 += 1
        # print(l, r, ":", xl, j1, j2, (j2 - j1))
        self.counter += (j2 - j1)
      # merge sort, return the sorted l, r combined, so O(NlogN) overall
      for i in range(len(nums) - 1, -1, -1):
        if l and r:
          nums[i] = l.pop() if l[-1] > r[-1] else r.pop()
        elif l:
          nums[i] = l.pop()
        else:
          nums[i] = r.pop()
    else:
      if nums and self.lower <= nums[0] <= self.upper:
        self.counter += 1
    return nums
  def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
    """Q0315, O(NlogN), divide and conquer, modified mergesort.
    """
    # nums: re-use to store partial sums of nums[0:(i+1)]
    for i in range(1, len(nums)):
      nums[i] += nums[i - 1]
    self.counter, self.lower, self.upper = 0, lower, upper
    self._mergesort(nums)
    return self.counter

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([0], -1, 1),
    ([-2,5,-1], -2, 2),
    ([-2,0,-2,-3,2,2,1,-3,4], 4, 11),
  ]
  rslts = [solver.countRangeSum(nums, lower, upper) for nums, lower, upper in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")