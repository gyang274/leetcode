class Solution:
  def findUnsortedSubarray(self, nums: List[int]) -> int:
    """O(NlogN)
    """
    arrs, n = sorted(nums), len(nums)
    i, j = 0, n - 1
    while i <= j and nums[i] == arrs[i]:
      i += 1
    while i <= j and nums[j] == arrs[j]:
      j -= 1
    return j - i + 1

class Solution:
  def findUnsortedSubarray(self, nums: List[int]) -> int:
    """O(N)
    """
    n = len(nums)
    if n == 0:
      return 0
    # left minimals
    stack = [nums[0]]
    i = 1
    while i < n and stack[-1] <= nums[i]:
      stack.append(nums[i])
      i += 1
    while i < n:
      while stack and stack[-1] > nums[i]:
        stack.pop()
      if not stack:
        break
      i += 1
    l = len(stack)
    # right maximals
    stack = [nums[-1]]
    i = n - 2
    while i >= 0 and nums[i] <= stack[-1]:
      stack.append(nums[i])
      i -= 1
    while i >= 0:
      while stack and nums[i] > stack[-1]:
        stack.pop()
      if not stack:
        break
      i -= 1
    r = len(stack)
    return max(0, n - (l + r))