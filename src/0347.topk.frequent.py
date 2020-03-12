from typing import List
from collections import defaultdict, Counter

import heapq

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    """priority queue, undocumented func for max heap, e.g., _heapify_max, _heappush_max, _heappop_max and etc.
    """
    cntr = Counter(nums)
    d = defaultdict(list)
    for i in cntr:
      d[cntr[i]].append(i)
    q = list(d.keys())
    heapq._heapify_max(q)
    x = []
    while len(x) < k:
      x.extend(d[heapq._heappop_max(q)])
    return x[:k]