from typing import List
from config.interval import Interval

class MyCalendar:

  def __init__(self):
    self.calendar = Interval()

  def book(self, start: int, end: int) -> bool:
    if self.calendar.cross(start, end):
      return False
    self.calendar.insert(start, end)
    return True