from typing import List

class Solution:
  def find132pattern(self, nums: List[int]) -> bool:
    """O(N), one pass, keep a set of none overlapped 13 intervals for 2.
    """
    # s: set of none overlapped 13 intervals
    # i: index track of 1 (min) of current none overlapped 13
    # j: index track of 3 (max) of current none overlapped 13
    s, i, j, n = set([]), 0, 1, len(nums)
    while j < n:
      for xmin, xmax in s:
        if xmin < nums[j] < xmax:
          return True
      if nums[j] <= nums[i]:
        i = j
      else:
        # for xmin, xmax in s:
        #   if nums[i] < xmin < nums[j] or nums[i] < xmax < nums[j] or xmin < nums[i] < xmax or xmin < nums[j] < xmax:
        #     s.remove((xmin, xmax))
        #     s.add((min(xmin, nums[i]), max(nums[j], xmax)))
        # else:
        #   s.add((nums[i], nums[j]))
        s.add((nums[i], nums[j]))
      j += 1
    return False

class Solution:
  def find132pattern(self, nums: List[int]) -> bool:
    """O(N), stack peek.
    """
    # mins: 1 for all i-th
    n, mins = len(nums), nums.copy()
    for i in range(1, n):
      mins[i] = min(mins[i - 1], mins[i])
    # stack: 2 for all i-th
    stack = []
    for i in range(n - 1, -1, -1):
      while stack and stack[-1] <= mins[i]:
        stack.pop()
      if stack and nums[i] > stack[-1]:
        return True
      elif not stack or stack[-1] > nums[i] > mins[i]:
        stack.append(nums[i])
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,2,3,4],
    [3,1,4,2],
    [-1,1,-2,2,-3,3,-4,4,-5,5],
    [-1,1,-2,2,-3,3,-4,4,-5,5,0],
    [3,5,0,3,4],
    [7,9,4,6,5]
  ]
  rslts = [solver.find132pattern(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")