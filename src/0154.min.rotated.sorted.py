from typing import List

class Solution:
  def findMin(self, nums: List[int]) -> int:
    """O(logN): modified binary search, similar to 0033 and 0081.
      How duplicate impact? For example, [3, 0, 1, 2, 3, 3, 3, 3, 3], nums[lft] == nums[mid] == num[rgt],
      in this case, don't know where to move, so shrink both side lft += 1 and rgt -= 1, so worst case O(n).
    """
    # if len(nums) == 0: return None
    l, r = 0, len(nums) - 1
    while l < r - 1 and nums[l] >= nums[r]:
      # m = l + (r - l) / 2, instead of m = (l + r) /2
      # This is done intentionally to prevent the numeric overflow issue, since the sum of two integers could exceed the
      # limit of the integer number. As a fun fact, the above mistake prevails in many implementations of binary search,
      # as revealed from a post titled "Nearly All Binary Searches and Mergesorts are Broken" from googleblog in 2006.
      m = l + (r - l) // 2
      if nums[l] == nums[m] == nums[r]:
        l += 1
        r -= 1
      else:
        if nums[l] <= nums[m]:
          l = m
        else:
          r = m
    return min(nums[l], nums[r])


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    # [],
    [1],
    [2,1],
    [3,1,2],
    [3,4,5,1,2],
    [4,5,6,7,0,1,2],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
  ]
  rslts = [solver.findMin(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  