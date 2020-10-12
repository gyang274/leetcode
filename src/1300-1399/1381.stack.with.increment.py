class CustomStack:

  def __init__(self, maxSize: int):
    self.smax = maxSize
    self.stack = []
  
  def push(self, x: int) -> None:
    if len(self.stack) < self.smax:
      self.stack.append(x)

  def pop(self) -> int:
    if self.stack:
      return self.stack.pop()
    return -1

  def increment(self, k: int, val: int) -> None:
    for i in range(min(len(self.stack), k)):
      self.stack[i] += val
  