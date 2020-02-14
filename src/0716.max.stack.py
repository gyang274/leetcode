class Node:
  """double linked list node with extra pointer to prev max.
  """
  def __init__(self, x):
    self.val = x
    # previous max node, on each max node, so when pop this node, move global pointer to its previous max node.
    self.max = None
    # prev node
    self.prev = None
    # next node
    self.next = None

class MaxStack:
  """O(1) on all operations, double linked list + extra pointer to prev max (on each max node) + global pointer to max.
    head <-> node (4) <-> node (5) <-> ... (all < 5) <-> node (8) <-> tail
              ^------------max ^------------------------------max
    4 is 5's prev max and 5 is 8's prev max, so               ^
    when popMax() update global max from 8 to 5               | global max
  issue:
    what is popMax, poMax until 4? ...
  """
  def __init__(self):
    """initialize your data structure here.
    """
    # init double linked list
    self.head = Node('')
    self.tail = Node('')
    self.head.next = self.tail
    self.tail.prev = self.head
    # global pointer to max node
    self.maxnode = None
  
  def push(self, x: int) -> None:

  def pop(self) -> int:

  def top(self) -> int:
      
  def peekMax(self) -> int:
      
  def popMax(self) -> int:
        
class MaxStack(list):
  """O(N): Two stack, store element (x, xmax), when popMax, pop top until max and then push back.
  """
  def push(self, x: int) -> None:
    m = max(x, self[-1][1] if self else None)
    self.append((x, m))

  def pop(self) -> int:
    return list.pop(self)[0]

  def top(self) -> int:
    return self[-1][0]

  def peekMax(self) -> int:
    return self[-1][1]

  def popMax(self) -> int:
    m = self[-1][1]
    b = []
    while self[-1][0] != m:
      b.append(self.pop())
    self.pop()
    map(self.push, reversed(b))
    return m