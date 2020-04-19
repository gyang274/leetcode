class MyCircularQueue:

  def __init__(self, k: int):
    """Initialize your data structure here. Set the size of the queue to be k.
    """
    self.queue = [None] * k
    self.init = 0
    self.ende = 0
    self.size = k

  def enQueue(self, value: int) -> bool:
    """Insert an element into the circular queue. Return true if the operation is successful.
    """
    if self.isFull():
      return False
    self.queue[self.ende] = value
    self.ende = (self.ende + 1) % self.size
    return True

  def deQueue(self) -> bool:
    """Delete an element from the circular queue. Return true if the operation is successful.
    """
    if self.isEmpty():
      return False
    self.queue[self.init] = None
    self.init = (self.init + 1) % self.size
    return True

  def Front(self) -> int:
    """Get the front item from the queue.
    """
    if self.isEmpty():
      return -1
    return self.queue[self.init]

  def Rear(self) -> int:
    """Get the last item from the queue.
    """
    if self.isEmpty():
      return -1
    return self.queue[(self.ende - 1) % self.size]

  def isEmpty(self) -> bool:
    """Checks whether the circular queue is empty or not.
    """
    return self.ende == self.init and self.queue[self.init] is None

  def isFull(self) -> bool:
    """Checks whether the circular queue is full or not.
    """
    return self.ende == self.init and self.queue[self.ende] is not None
