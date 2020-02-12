# OrderedDict
from collections import OrderedDict

class LRUCache(OrderedDict):
  def __init__(self, capacity: int):
    """OrderedDict
    """
    self.capacity = capacity
  def get(self, key: int) -> int:
    if key in self:
      self.move_to_end(key)
    return super(LRUCache, self).get(key, -1)
  def put(self, key: int, value: int) -> None:
    if key in self:
      self.move_to_end(key)
    self[key] = value
    while len(self) > self.capacity:
      self.popitem(last=False)


# Hashmap + DoubleLinkedList
class DoubleLinkedListNode():
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None
    self.prev = None

class LRUCache():
  def __init__(self, capacity: int):
    self.cache = {}
    self.capacity = capacity
    self.head = DoubleLinkedListNode('', '')
    self.tail = DoubleLinkedListNode('', '')
    self.head.next = self.tail
    self.tail.prev = self.head
  def get(self, key: int) -> int:
    if key in self.cache:
      node = self.cache[key]
      self._move_to_head(node)
      return node.value
    return -1
  def put(self, key: int, value: int) -> None:
    if key in self.cache:
      node = self.cache[key]
      self._move_to_head(node)
      # update the value
      node.value = value
    else:
      node = DoubleLinkedListNode(key, value)
      self._insert_node(node)
      self.cache[key] = node
    while len(self.cache) > self.capacity:
      node = self._pop_from_tail()
      self.cache.pop(node.key)
  # aux node operations
  def _insert_node(self, node):
    """insert node after head.
    """
    node.prev = self.head
    node.next = self.head.next
    node.next.prev = node
    self.head.next = node
  def _remove_node(self, node):
    """remove node.
    """
    node.prev.next = node.next
    node.next.prev = node.prev
    # node.next = None
    # node.prev = None
  def _move_to_head(self, node):
    self._remove_node(node)
    self._insert_node(node)
  def _pop_from_tail(self):
    if not self.tail.prev == self.head:
      node = self.tail.prev
      self._remove_node(node)
      return node
    return None


# # Hashmap + PriorityQueue 
# # PriorityQueue requires Fibonacci Heap so that decrease-key operation is O(1)
# # unfortunately, in-place, e.g., decrease-key/increase-key are not supported by nature, pop and push requires O(logN)
# import heapq

# class LRUCache():
#   def __init__(self, capacity: int):
#     self.capacity = capacity
#     self.cache = {}
#     self.queue = []
#     self.timer = 1
#     heapq.heapify(self.queue)
#   def get(self, key: int) -> int:
#     if key in self.cache:
#       node = self.cache[key]
#       # update the recency
#       node[0] = self.timer
#       self.timer += 1
#       return node[2]
#     return -1
#   def put(self, key: int, value: int) -> None:
#     if key in self.cache:
#       node = self.cache[key]
#       # update recency
#       node[0] = self.timer
#       # update the value
#       node[2] = value
#     else:
#       if len(self.cache) == self.capacity:
#         # # in-place change the least recent unit, instead of push new and pop old
#         node = self.queue[0]
#         self.cache.pop(node[1])
#         node[0] = self.timer
#         node[1] = key
#         node[2] = value
#         self.cache[key] = node
#       else:
#         node = [self.timer, key, value]
#         heapq.heappush(self.queue, node)
#         self.cache[key] = node
#     self.timer += 1
    

if __name__ == '__main__':
  x = LRUCache(capacity = 2)
  print(x.put(1, 1))
  print(x.put(2, 2))
  print(x.get(1))
  print(x.put(3, 3))
  print(x.get(2))
  print(x.put(4, 4))
  print(x.get(1))
  print(x.get(3))
  print(x.get(4))