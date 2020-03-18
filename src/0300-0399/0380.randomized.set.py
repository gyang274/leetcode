class RandomizedSet:

  def __init__(self):
    """Initialize your data structure here.
    """
    self.s = set([])
    

  def insert(self, val: int) -> bool:
    """Inserts a value to the set. Returns true if the set did not already contain the specified element.
    """
    if val in self.s:
      return False
    self.s.add(val)
    return True

  def remove(self, val: int) -> bool:
    """Removes a value from the set. Returns true if the set contained the specified element.
    """
    if val not in self.s:
      return False
    self.s.remove(val)
    return True

  def getRandom(self) -> int:
    """Get a random element from the set.
    """
    # pop(): Remove and return an arbitrary element from the set. Raises KeyError if the set is empty.
    if self.s:
      x = self.s.pop()
      self.s.add(x)
      return x
    return -1

# HashMap + ArrayList
import random

class RandomizedSet:
  """HashMap + ArrayList
    To delete a value at arbitrary index takes linear time. The solution here is to always delete the last value:
      Swap the element to delete with the last one.
      Pop the last element out.
  """

  def __init__(self):
    """Initialize your data structure here.
    """
    # d: val -> idx
    self.dict = dict()
    self.list = list()
    
  def insert(self, val: int) -> bool:
    """Inserts a value to the set. Returns true if the set did not already contain the specified element.
    """
    if val in self.dict:
      return False
    self.dict[val] = len(self.list)
    self.list.append(val)
    return True

  def remove(self, val: int) -> bool:
    """Removes a value from the set. Returns true if the set contained the specified element.
    """
    if val not in self.dict:
      return False
    # swap this val with the last val in list
    idx = self.dict[val]
    self.dict[self.list[-1]] = idx
    self.list[idx] = self.list[-1]
    self.list.pop()
    self.dict.pop(val)
    return True

  def getRandom(self) -> int:
    """Get a random element from the set.
    """
    return random.choice(self.list)
