import heapq

class DinnerPlates:

  def __init__(self, capacity: int):
    self.size = capacity
    self.stackes = []
    self.pointer = []

  def push(self, val: int) -> None:
    if self.pointer:
      if self.pointer[0] < len(self.stackes):
        self.stackes[heapq.heappop(self.pointer)].append(val)
        return None
      else:
        self.pointer = []
    if not (self.stackes and len(self.stackes[-1]) < self.size):
      self.stackes.append([])
    self.stackes[-1].append(val)

  def pop(self) -> int:
    while self.stackes and not self.stackes[-1]:
      self.stackes.pop()
    if self.stackes:
      return self.stackes[-1].pop()
    return -1

  def popAtStack(self, index: int) -> int:
    if index < len(self.stackes) and self.stackes[index]:
      heapq.heappush(self.pointer, index)
      return self.stackes[index].pop()
    return -1