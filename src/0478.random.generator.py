import math
import random

class Solution:
  def __init__(self, radius: float, x_center: float, y_center: float):
    self.radius = radius
    self.x = x_center
    self.y = y_center
  def randPoint(self) -> List[float]:
    # theta
    t = random.random() * math.pi * 2
    # dists
    r = math.sqrt(random.random()) * self.radius
    return [self.x + r * math.cos(t), self.y + r * math.sin(t)]
