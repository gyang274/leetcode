from collections import deque

class MyStack:
  """implement stack using 2 queues:
    1. make push() cost O(1), pop() cost O(N): 
      push() into queue0, pop() from queue0 and push() into queue1 until get last element from queue0, swap q0 and q1.
    2. make push() cost O(N), pop() cost O(1):
      pop() from queue0 left, make sure left is last, so when push(), push() to queue1 and pop() all one by one from 
      queue0 and push() to queue1, and swap q0 and q1, also top() is same as peek from left.
  """
  def __init__(self):
    """Initialize your data structure here.
    """
    self.q0 = deque([])
    self.q1 = deque([])

  def push(self, x: int) -> None:
    """Push element x onto stack.
    """
    self.q1.append(x)
    while self.q0:
      self.q1.append(self.q0.popleft())
    self.q0, self.q1 = self.q1, self.q0
    
  def pop(self) -> int:
    """Removes the element on top of the stack and returns that element.
    """
    return self.q0.popleft()
    
  def top(self) -> int:
    """Get the top element.
    """
    return self.q0[0]

  def empty(self) -> bool:
    """Returns whether the stack is empty.
    """
    return not self.q0

class MyStack:
  """implement stack using 1 queue:
    1. make push() cost O(N), pop() cost O(1):
      pop() from queue left, make sure left is last, so when push(), push() to queue as last one then pop() from front
      and push back until the last one is in front, as such that elements in queue are rotated so last one is in front
  """
  def __init__(self):
    """Initialize your data structure here.
    """
    self.queue = deque([])

  def push(self, x: int) -> None:
    """Push element x onto stack.
    """
    # number of elements in queue
    n = len(self.queue)
    # push x into the back as last
    self.queue.append(x)
    # rotated out/in all elements in front of x so x is the first element
    for _ in range(n):
      self.queue.append(self.queue.popleft())
    
  def pop(self) -> int:
    """Removes the element on top of the stack and returns that element.
    """
    return self.queue.popleft()
    
  def top(self) -> int:
    """Get the top element.
    """
    return self.queue[0]

  def empty(self) -> bool:
    """Returns whether the stack is empty.
    """
    return not self.queue
        