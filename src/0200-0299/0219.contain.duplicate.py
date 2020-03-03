from typing import List
from collections import defaultdict

class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    """Hash value -> index set.
    """
    xdict = defaultdict(list)
    for i, x in enumerate(nums):
      xdict[x].append(i)
    for x, v in xdict.items():
      for i in range(len(v)):
        for j in range(i + 1, len(v)):
          if v[j] - v[i] <= k:
            return True
    return False

class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    """Hash table with a sliding window of size k.
    """
    xdict = set()
    for i in range(len(nums)):
      if i > (k + 1):
        xdict.remove(nums[i - k - 1])
      if nums[i] in xdict:
        return True
      xdict.add(nums[i])
    return False

      
