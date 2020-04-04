from typing import List

class Solution:
  def findDuplicates(self, nums: List[int]) -> List[int]:
    # a[i] == i + 1 when no duplicates
    i, n, ans = 0, len(nums), set([])
    while i < n:
      if nums[i] == i + 1:
        i += 1
      elif nums[i] == nums[nums[i] - 1]:
        ans.add(nums[i])
        i += 1
      else:
        j = nums[i] - 1
        nums[i], nums[j] = nums[j], nums[i]
    return ans

class Solution(object):
  def findDuplicates(self, nums: List[int]) -> List[int]:
    """use the array index itself indicates a num seen or not.
    """
    ans = []
    for x in nums:
      if nums[abs(x) - 1] < 0:
        ans.append(abs(x))
      else:
        nums[abs(x) - 1] *= -1
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [1],
    [1,1],
    [1,1,2,2,3,4,5],
    [4,3,2,7,8,2,3,1],
  ]
  rslts = [solver.findDuplicates(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
