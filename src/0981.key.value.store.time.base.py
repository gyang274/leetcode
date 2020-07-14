from collections import defaultdict

import bisect

class TimeMap:

  def __init__(self):
    """Initialize your data structure here.
    """
    self.d = defaultdict(list)

  def set(self, key: str, value: str, timestamp: int) -> None:
    self.d[key].append((timestamp, value))
    
  def get(self, key: str, timestamp: int) -> str:
    i = bisect.bisect_right(self.d[key], (timestamp, '\x7f'))
    if i == 0:
      return ""
    return self.d[key][i - 1][1]
