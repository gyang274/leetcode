from collections import Counter

class Solution:
  def findLHS(self, nums: List[int]) -> int:
    counter = Counter(nums)
    maxlen = 0
    for k in counter:
      if k + 1 in counter:
        maxlen = max(maxlen, counter[k] + counter[k + 1])
    return maxlen