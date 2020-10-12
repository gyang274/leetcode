from typing import List
from collections import defaultdict

import bisect

class TweetCounts:

  def __init__(self):
    self.T = defaultdict(lambda: [False, []])

  def recordTweet(self, tweetName: str, time: int) -> None:
    self.T[tweetName][0] = False
    self.T[tweetName][1].append(time)

  def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
    delta = 60 if freq == 'minute' else 3600 if freq == 'hour' else 86400
    if not self.T[tweetName][0]:
      self.T[tweetName][1].sort()
      self.T[tweetName][0] = True
    ans = []
    s = startTime
    i = bisect.bisect_left(self.T[tweetName][1], s)
    while s <= endTime:
      e = min(s + delta, endTime + 1)
      j = bisect.bisect_left(self.T[tweetName][1], e)
      ans.append(j - i)
      s, i = e, j
    return ans
