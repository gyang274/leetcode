from collections import deque

class RecentCounter:

  def __init__(self):
    self.queue = deque([])

  def ping(self, t: int) -> int:
    while self.queue and t - self.queue[0] > 3000:
      self.queue.popleft()
    self.queue.append(t)
    return len(self.queue)
