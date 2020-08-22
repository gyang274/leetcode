from collections import defaultdict

import bisect

class MajorityChecker:

  def __init__(self, arr: List[int]):
    # d: value -> indices
    self.d = defaultdict(list)
    # Q0458, index each value by binary, in or not in 15 groups, 2^5 = 32768 > 20000.
    self.q = [[0] * 15 for _ in range(len(arr) + 1)]
    for i, x in enumerate(arr):
      self.d[x].append(i)
      for j in range(15):
        self.q[i + 1][j] = self.q[i][j] + (x & 1)
        x >>= 1
    
  def query(self, left: int, right: int, threshold: int) -> int:
    # candidate
    x = 0
    for j in range(15):
      if self.q[right + 1][j] - self.q[left][j] >= threshold:
        x |= 1 << j
    return x if bisect.bisect_right(self.d[x], right) - bisect.bisect_left(self.d[x], left) >= threshold else -1
