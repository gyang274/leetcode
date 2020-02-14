class MinStack:
  """maintain a dict self.mindnext such that each min point to previous min, so when pop is min, update min with O(1).
  """
  def __init__(self):
    """initialize your data structure here.
    """
    self.minvalue = None
    self.mindnext = {}
    self.valstack = []

  def push(self, x: int) -> None:
    self.valstack.append(x)
    if self.minvalue is None or x <= self.minvalue:
      if self.minvalue is None or x < self.minvalue:
        self.mindnext[x] = [self.minvalue, 1]
        self.minvalue = x
      else:
        # x == self.minvalue, so after pop still same minvalue,
        # like a self-loop in dict, e.g., self.mindnext[x] = x,
        # but cannot have duplicate key, so use the 1st dict value 
        # to represent how many times seen this key at this state.
        self.mindnext[x][1] += 1

  def pop(self) -> None:
    x = self.valstack.pop()
    if x == self.minvalue:
      if self.mindnext[self.minvalue][1] == 1:
        self.minvalue, _ = self.mindnext.pop(self.minvalue)
      else:
        self.mindnext[self.minvalue][1] -= 1

  def top(self) -> int:
    return self.valstack[-1]

  def getMin(self) -> int:
    return self.minvalue

from collections import deque
class MinStack:
  """maintain an extra minvalue at each node, more memory for lazy logic.
  """
  def __init__(self):
    """initialize your data structure here.
    """
    self.stack = deque([])
    
  def push(self, x: int) -> None:
    if self.stack:
      xmin = self.stack[-1][1]
    else:
      xmin = x
    self.stack.append((x, min(x, xmin)))

  def pop(self) -> None:
    self.stack.pop()
    
  def top(self) -> int:
    return self.stack[-1][0]

  def getMin(self) -> int:
    return self.stack[-1][1]

if __name__ == '__main__':
  minStack = MinStack()
  print(minStack.push(-2))
  print(minStack.push(0))
  print(minStack.push(-3))
  # return -3
  print(minStack.getMin())
  print(minStack.pop())
  # return 0
  print(minStack.top())
  # return -2
  print(minStack.getMin())

  # ["MinStack","push","push","push","push","getMin","pop","getMin","pop","getMin","pop","getMin"]
  # [[],[2],[0],[3],[0],[],[],[],[],[],[],[]]

  # ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
  # [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]