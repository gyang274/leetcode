from collections import Counter

import itertools

class Solution:
  def frequencySort(self, nums: List[int]) -> List[int]:
    d = Counter(nums)
    x = sorted([[-d[k], k] for k in d], reverse=True)
    return list(itertools.chain(*[[v] * -k for k, v in x]))
