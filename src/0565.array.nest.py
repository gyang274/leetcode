from typing import List

class Solution:
  def arrayNesting(self, nums: List[int]) -> int:
    """TC: O(N), SC: O(N).
    """
    maxlen, unseen = 0, set(nums)
    while unseen:
      x, seen = unseen.pop(), set([])
      while x not in seen:
        seen.add(x)
        x = nums[x]
        unseen.discard(x)
      maxlen = max(maxlen, len(seen))
    return maxlen

class Solution:
  def arrayNesting(self, nums: List[int]) -> int:
    """TC: O(N), SC: O(1).
    """
    maxlen, n = 0, len(nums)
    for i in range(n):
      if nums[i] > -1:
        x, count = i, 0
        while nums[x] > -1:
          z = nums[x]
          nums[x] = -1
          x = z
          count += 1
        maxlen = max(maxlen, count)
    return maxlen

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [5,4,0,3,1,6,2],
  ]
  rslts = [solver.arrayNesting(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
