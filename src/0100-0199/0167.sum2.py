class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    """numbers are sorted, so index from both side as two pointers.
    """
    l, r = 0, len(numbers) - 1
    while l < r:
      xsum = numbers[l] + numbers[r]
      if xsum == target:
        return l + 1, r + 1
      elif xsum < target:
        l += 1
      else:
        r -= 1
    return None