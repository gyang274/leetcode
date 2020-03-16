from collections import defaultdict

import random

class RandomizedCollection:
  """Q0380, HashMap + ArrayList
  """

  def __init__(self):
    """Initialize your data structure here.
    """
    self.dict = defaultdict(set)
    self.list = []

  def insert(self, val: int) -> bool:
    """Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
    """
    unseen = val not in self.dict
    self.dict[val].add(len(self.list))
    self.list.append(val)
    return unseen

  def remove(self, val: int) -> bool:
    """Removes a value from the collection. Returns true if the collection contained the specified element.
    """
    if val not in self.dict:
      return False
    # swap this val with the last val in list
    idx = self.dict[val].pop()
    if not self.dict[val]:
      self.dict.pop(val)
    if idx < len(self.list) - 1:
      self.dict[self.list[-1]].discard(len(self.list) - 1)
      self.dict[self.list[-1]].add(idx)
      self.list[idx] = self.list[-1]
    self.list.pop()
    return True

  def getRandom(self) -> int:
    """Get a random element from the collection.
    """
    return random.choice(self.list)
