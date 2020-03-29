class Solution:
  def minMoves2(self, nums: List[int]) -> int:
    xm = median(nums)
    return int(sum([abs(x - xm) for x in nums]))

class Solution:
  def minMoves2(self, nums: List[int]) -> int:
    """max and min are equal to same x, min <= x <= max at the end when all equal,
      so (max - x) + (x - min) = (max - min) is the total move of min and max.
    """
    nums.sort()
    i, n, moves = 0, len(nums), 0
    while i < n // 2:
      moves += nums[n - 1 - i] - nums[i]
      i += 1
    return moves

class Solution:
  def minMoves2(self, nums: List[int]) -> int:
    """O(N): median of medians, n // 5 groups.
    """
    return NotImplemented