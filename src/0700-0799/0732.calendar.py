from typing import List
from config.interval import Interval

class MyCalendarThree:

  def __init__(self):
    self.calendars = []

  def book(self, start: int, end: int) -> int:
    queue = [start, end]
    for i, calendar in enumerate(self.calendars):
      qnext = []
      for s, e in zip(*[iter(queue)]*2):
        # TODO: insert and return cross in the same step.
        qnext.extend(calendar.cross(s, e))
        self.calendars[i].insert(s, e)
      queue = qnext
      if not queue:
        break
    if queue:
      self.calendars.append(Interval(queue))
    return len(self.calendars)