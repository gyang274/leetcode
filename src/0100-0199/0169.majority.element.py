from typing import List

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    """annihilation: delete both element i and j when not nums[i] == nums[j], 
      since majority even in worst case whatever left is the single majority.
    """
    stack, i, n = [nums[0], ], 1, len(nums)
    while i < n:
      if not stack or nums[i] == stack[-1]:
        stack.append(nums[i])
      else:
        stack.pop()
      i += 1
    return stack[0]

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    """annihilation: delete both element i and j when not nums[i] == nums[j], 
      since majority even in worst case whatever left is the single majority.
      improvement: keep a value and count, no need to keep a stack as at most one value in stack, and append is costly.
    """
    x, count, i, n = None, 0, 0, len(nums)
    while i < n:
      if count == 0:
        x = nums[i]
        count = 1
      elif nums[i] == x:
        count += 1
      else:
        count -= 1
      i += 1
    return x

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    """annihilation: delete both element i and j when not nums[i] == nums[j], 
      since majority even in worst case whatever left is the single majority.
      improvement: keep a value and count, no need to keep a stack as at most one value in stack, and append is costly.
    """
    s, count = None, 0
    for x in nums:
      if count == 0:
        s = x
        count = 1
      elif x == s:
        count += 1
      else:
        count -= 1
    return s

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1],
    [1,1],
    [1,1,2],
    [1,1,2,2,2],
  ]
  rslts = [solver.majorityElement(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")