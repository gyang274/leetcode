from typing import List
from collections import Counter

import heapq

class Solution:
  def topKFrequent(self, words: List[str], k: int) -> List[str]:
    wc = [(-v, k) for k, v in Counter(words).items()]
    # priority queue
    heapq.heapify(wc)
    return [heapq.heappop(wc)[1] for _ in range(k)]
        