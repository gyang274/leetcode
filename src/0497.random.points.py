import random

class Solution:

  def __init__(self, rects: List[List[int]]):
    self.rects = rects
    self.numpt = [(x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rects]

  def pick(self) -> List[int]:
    rect = random.choices(self.rects, self.numpt)[0]
    return [random.randint(rect[0], rect[2]), random.randint(rect[1], rect[3])]