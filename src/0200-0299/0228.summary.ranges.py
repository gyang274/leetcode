from typing import List

class Solution:
  def summaryRanges(self, nums: List[int]) -> List[str]:
    if not nums:
      return []
    # init with 0
    x, r, stack = str(nums[0]), False, []
    # go through nums
    for i in range(1, len(nums)):
      if nums[i] == nums[i - 1] + 1:
        r = True
      else:
        if r:
          x += "->" + str(nums[i - 1])
        stack.append(x)
        x, r = str(nums[i]), False
    # ende with -1
    if r:
      x += "->" + str(nums[-1])
    stack.append(x)
    return stack

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [0,1,2,4,5,7],
    [0,2,3,4,6,8,9],
  ]
  rslts = [solver.summaryRanges(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")