from typing import List

class Solution:
  def findPeakElement(self, nums: List[int]) -> int:
    """modified binary search.
      noticed the condition that nums[i] != nums[i+1], otherwise, say nums = [2] * N, then O(logN) is impossible.
    """
    n = len(nums)
    if n == 0: 
      return None
    l, r = 0, n - 1
    while l <= r:
      # m = (l + r) // 2 ? no, overflow!
      m = l + (r - l) // 2
      # nums[m - 1] < nums[m] and nums[m] > nums[m + 1]
      if (m == 0 or nums[m - 1] < nums[m]) and (m == n - 1 or nums[m] > nums[m + 1]):
        return m
      # -inf < nums[0] ... nums[m - 1] > nums[m] > nums[m + 1] 
      # ---------------------- then l, m must has some valley
      elif m > 0 and nums[m - 1] > nums[m]:
        r = m - 1
      # nums[m - 1] < nums[m] < nums[m + 1] ... nums[n - 1] > -inf
      #              ---------------------- then m, r must has some valley
      # elif m < n - 1 and nums[m] < nums[m + 1]:
      else:
        l = m + 1
    return m

class Solution:
  def findPeakElement(self, nums: List[int]) -> int:
    """modified binary search.
      noticed the condition that nums[i] != nums[i+1], otherwise, say nums = [2] * N, then O(logN) is impossible.
    """
    l, r = 0, len(nums) - 1
    while l < r:
      m = l + (r - l) // 2
      if (nums[m] > nums[m + 1]):
        r = m
      else:
        l = m + 1
    return l

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [],
    [1],
    [1,2],
    [1,2,3,1],
    [1,2,1,3,5,6,4],
  ]
  rslts = [solver.findPeakElement(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")