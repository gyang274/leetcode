import random

class DoubleLinkedList:
  def __init__(self, val = None):
    self.val = val
    self.next = None
    self.prev = None

class AllOne:
  """Q0380, Q0381, HashMap + LinkedList + RandomizedSet
  """

  def __init__(self):
    """Initialize your data structure here.
    """
    # dict of key -> DLL([val, (keys)])
    self.dict = {}
    # double linked list head and tail, head <-> tail
    self.head = DoubleLinkedList([ 0, set([])])
    self.tail = DoubleLinkedList([-1, set([])])
    self.head.next = self.tail
    self.tail.prev = self.head

  def inc(self, key: str) -> None:
    """Inserts a new key <Key> with value 1. Or increments an existing key by 1.
    """
    if key not in self.dict:
      self.dict[key] = self.head
      self.head.val[1].add(key)
    # node: [value, set([keys with same value])]
    node = self.dict[key]
    node.val[1].remove(key)
    # move key to node with value + 1, create if not exists
    if node.next.val[0] == node.val[0] + 1:
      self.dict[key] = node.next
    else:
      nuxt = DoubleLinkedList([node.val[0] + 1, set([])])
      self.dict[key] = nuxt
      # insert nuxt to dll
      nuxt.next = node.next
      node.next.prev = nuxt
      node.next = nuxt
      nuxt.prev = node
    node.next.val[1].add(key)
    # remove node if set([keys with same value]) is empty
    if not (node == self.head or node.val[1]):
      node.prev.next = node.next
      node.next.prev = node.prev
      del node
    return None

  def dec(self, key: str) -> None:
    """Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
    """
    if key in self.dict:
      node = self.dict[key]
      node.val[1].remove(key)
      if node.prev.val[0] == node.val[0] - 1:
        self.dict[key] = node.prev
      else:
        pruv = DoubleLinkedList([node.val[0] - 1, set([])])
        self.dict[key] = pruv
        # insert prev to dll
        node.prev.next = pruv
        pruv.prev = node.prev
        node.prev = pruv
        pruv.next = node
      node.prev.val[1].add(key)
      # remove node if set([keys with same value]) is empty
      if not node.val[1]:
        node.prev.next = node.next
        node.next.prev = node.prev
        del node
    return None

  def getMaxKey(self) -> str:
    """Returns one of the keys with maximal value.
    """
    # if init self.head.val[1] as set([""]), issue if insert a key "" and delete this key..
    if self.tail.prev == self.head:
      return ""
    return random.choice(list(self.tail.prev.val[1]))
    
  def getMinKey(self) -> str:
    """Returns one of the keys with Minimal value.
    """
    if self.head.next == self.tail:
      return ""
    return random.choice(list(self.head.next.val[1]))