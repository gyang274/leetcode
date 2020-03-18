from typing import List
from collections import deque

class Solution:
  def countSmaller(self, nums: List[int]) -> List[int]:
    """Q0300, longest increase sequence.
      modified binary search, reverse, from right to left, for each x binary search on index of largest < x.
    """
    ans, stack = deque([]), []
    for x in reversed(nums):
      l, r = 0, len(stack)
      while l < r:
        m = l + (r - l) // 2
        if x <= stack[m]:
          r = m
        else:
          l = m + 1
      # insert is 20x faster..
      # stack = stack[:l] + [x] + stack[l:]
      stack.insert(l, x)
      ans.appendleft(l)
    return ans

class Solution:
  def _mergesort(self, enums):
    """Args
      enums: (index, value) of nums, index to write back the jumps.
    """
    m = len(enums) // 2
    if m > 0:
      l, r = self._mergesort(enums[:m]), self._mergesort(enums[m:])
      for i in range(len(enums) - 1, -1, -1):
        if (not r) or (l and l[-1][1] > r[-1][1]):
          # all values in current r are less than this left, all jump over, accumlate it.
          self.ans[l[-1][0]] += len(r)
          enums[i] = l.pop()
        else:
          enums[i] = r.pop()
    return enums
  def countSmaller(self, nums: List[int]) -> List[int]:
    """mergesort, num of smaller after is num of right-to-left jump over in merge sort, accumulate from each recursion.
    """
    self.ans = [0] * len(nums)
    self._mergesort(list(enumerate(nums)))
    return self.ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [5,2,2,3,2],
  ]
  rslts = [solver.countSmaller(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")