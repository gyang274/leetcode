from typing import List

class Solution:
  def wiggleMaxLength(self, nums: List[int]) -> int:
    """dynamic programming: O(N)
      up[i]: max wiggle sequence end at i trending upward
      dn[i]: max wiggle sequence end at i trending downward
    """
    n = len(nums)
    if n < 2:
      return n
    up = [1] * n
    dn = [1] * n
    for i in range(1, n):
      if nums[i] == nums[i - 1]:
        up[i] = up[i - 1]
        dn[i] = dn[i - 1]
      elif nums[i] > nums[i - 1]:
        up[i] = dn[i - 1] + 1
        dn[i] = dn[i - 1]
      else:
        up[i] = up[i - 1]
        dn[i] = up[i - 1] + 1
    return max(up[n - 1], dn[n - 1])

class Solution:
  def wiggleMaxLength(self, nums: List[int]) -> int:
    """dynamic programming -> status machine, TC: O(N), SC: O(1)
    """
    n = len(nums)
    if n < 2:
      return n
    up = 1
    dn = 1
    for i in range(1, n):
      if nums[i] > nums[i - 1]:
        up = dn + 1
      elif nums[i] < nums[i - 1]:
        dn = up + 1
    return max(up, dn)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [0],
    [0,0],
    [0,1],
    [3,2],
    [0,1,2],
    [0,0,0,0,0,1],
    [1,4,2,8,5,7],
    [4,2,8,5,7,1],
    [1,17,5,10,13,15,10,5,16,8],
  ]
  rslts = [solver.wiggleMaxLength(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")