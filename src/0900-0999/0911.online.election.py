from typing import List
from collections import defaultdict

import bisect, heapq

class TopVotedCandidate:
  def __init__(self, persons: List[int], times: List[int]):
    self.times = times
    # leads at times
    self.leads = []
    # priority queue of leading candidate across time
    d, pq = defaultdict(lambda: 0), []
    for i, p in enumerate(persons):
      d[p] += 1
      heapq.heappush(pq, (-d[p], -i, p))
      self.leads.append(pq[0][2])

  def q(self, t: int) -> int:
    return self.leads[bisect.bisect_right(self.times, t) - 1]

class TopVotedCandidate:

  def __init__(self, persons: List[int], times: List[int]):
    self.times = times
    # leads across times
    self.leads = []
    lead, vote, count = None, 0, defaultdict(lambda: 0)
    for i, p in enumerate(persons):
      count[p] += 1
      if count[p] >= vote:
        lead, vote = p, count[p]
      self.leads.append(lead)
  
  def q(self, t: int) -> int:
    return self.leads[bisect.bisect_right(self.times, t) - 1]
