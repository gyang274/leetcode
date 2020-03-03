class MyQueue:
  """implement queue using 2 stacks:
    1. make push() cost O(N), pop and peek cost O(1), refr Q0225.
  """
  def __init__(self):
    """Initialize your data structure here.
    """
    self.s1 = []
    self.s2 = []
    
  def push(self, x: int) -> None:
    """Push element x to the back of queue.
    """
    while self.s1:
      self.s2.append(self.s1.pop())
    self.s1.append(x)
    while self.s2:
      self.s1.append(self.s2.pop())

  def pop(self) -> int:
    """Removes the element from in front of queue and returns that element.
    """
    return self.s1.pop()
    
  def peek(self) -> int:
    """Get the front element.
    """
    return self.s1[-1]
    
  def empty(self) -> bool:
    """Returns whether the queue is empty.
    """
    return not self.s1

class MyQueue:
  """implement queue using 2 stacks:
    1. make push() cost O(1), pop and peek cost amortized O(1) with lazy reverse.
    improvement, push() to stack1, reversed into stack2 when needed and pop() from stack2, once reversed order leave it.
  """
  def __init__(self):
    """Initialize your data structure here.
    """
    self.s1 = []
    self.s2 = []
    
  def push(self, x: int) -> None:
    """Push element x to the back of queue.
    """
    self.s1.append(x)
    
  def pop(self) -> int:
    """Removes the element from in front of queue and returns that element.
    """
    # self.s2 keep the early items (than self.s1) in reverse order
    if not self.s2:
      while self.s1:
        self.s2.append(self.s1.pop())
    return self.s2.pop()
    
  def peek(self) -> int:
    """Get the front element.
    """
    if not self.s2:
      while self.s1:
        self.s2.append(self.s1.pop())
    return self.s2[-1]
    
  def empty(self) -> bool:
    """Returns whether the queue is empty.
    """
    return not (self.s2 or self.s1)