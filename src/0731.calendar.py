from typing import List
from config.interval import Interval

class MyCalendarTwo:

  def __init__(self):
    self.calendar1 = Interval()
    self.calendar2 = Interval()
  
  def book(self, start: int, end: int) -> bool:
    cross = self.calendar1.cross(start, end)
    if not cross:
      self.calendar1.insert(start, end)
    else:
      for x, y in zip(*[iter(cross)]*2):
        if self.calendar2.cross(x, y):
          return False
      self.calendar1.insert(start, end)
      for x, y in zip(*[iter(cross)]*2):
        self.calendar2.insert(x, y)
    return True
