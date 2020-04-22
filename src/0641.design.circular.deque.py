class MyCircularDeque:

  def __init__(self, k: int):
    """Initialize your data structure here. Set the size of the deque to be k.
      deque = reverse(stack1) + stack2
    """
    self.size = k
    self.stack1 = []
    self.stack2 = []

  def insertFront(self, value: int) -> bool:
    """Adds an item at the front of Deque. Return true if the operation is successful.
    """
    if self.isFull():
      return False
    self.stack1.append(value)
    return True

  def insertLast(self, value: int) -> bool:
    """Adds an item at the rear of Deque. Return true if the operation is successful.
    """
    if self.isFull():
      return False
    self.stack2.append(value)
    return True

  def deleteFront(self) -> bool:
    """Deletes an item from the front of Deque. Return true if the operation is successful.
    """
    if self.isEmpty():
      return False
    if not self.stack1:
      while self.stack2:
        self.stack1.append(self.stack2.pop())
    self.stack1.pop()
    return True

  def deleteLast(self) -> bool:
    """Deletes an item from the rear of Deque. Return true if the operation is successful.
    """
    if self.isEmpty():
      return False
    if not self.stack2:
      while self.stack1:
        self.stack2.append(self.stack1.pop())
    self.stack2.pop()
    return True

  def getFront(self) -> int:
    """Get the front item from the deque.
    """
    if self.isEmpty():
      return -1
    elif self.stack1:
      return self.stack1[-1]
    else:
      return self.stack2[0]
    
  def getRear(self) -> int:
    """Get the last item from the deque.
    """
    if self.isEmpty():
      return -1
    elif self.stack2:
      return self.stack2[-1]
    else:
      return self.stack1[0]
    
  def isEmpty(self) -> bool:
    """Checks whether the circular deque is empty or not.
    """
    return not (self.stack1 or self.stack2)
    
  def isFull(self) -> bool:
    """Checks whether the circular deque is full or not.
    """
    return len(self.stack1) + len(self.stack2) >= self.size
