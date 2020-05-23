"""Definition for an Interval.
class Interval:
  def __init__(self, start: int = None, end: int = None):
    self.start = start
    self.end = end
"""

from config.interval import Interval as IntervalModule

class Solution:
  def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
    intervalModule = IntervalModule()
    for s in schedule:
      for interval in s:
        intervalModule.insert(interval.start, interval.end)
    freeTime = []
    for i in range(1, len(intervalModule.ranges) - 1, 2):
      freeTime.append(Interval(intervalModule.ranges[i], intervalModule.ranges[i + 1]))
    return freeTime

class Solution:
  def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
    """O(NlogN): line sweep.
    """
    events = []
    for employee in schedule:
      for interval in employee:
        events.append((interval.start, 0))
        events.append((interval.end, 1))
    events.sort()
    freeTime = []
    prev, on = None, 0
    for t, se in events:
      if on == 0 and prev is not None:
        freeTime.append(Interval(prev, t))
      on += 1 if se == 0 else -1
      prev = t
    return freeTime
