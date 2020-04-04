from config.listnode import ListNode, listToListNode

class Node:
  def __init__(self, val):
    self.val = val
    self.prev = None
    self.next = None

class DLinkedList:
  def __init__(self):
    # sentinel head node
    self.head = Node('')
    self.head.next = self.head.prev = self.head
    # double linked list size
    self.size = 0

  def __len__(self):
    return self.size

  def delete(self, node):
    """delete node from double linked list
    """
    node.prev.next = node.next
    node.next.prev = node.prev
    self.size -= 1

  def insertA(self, knot, node):
    """insert node after knot in double linked list
    """
    knot.next.prev = node
    node.next = knot.next
    knot.next = node
    node.prev = knot
    self.size += 1

  def insertB(self, knot, node):
    """insert node before knot in double linked list
    """
    knot.prev.next = node
    node.prev = knot.prev
    knot.prev = node
    node.next = knot
    self.size += 1

  def append(self, node):
    self.insertB(self.head, node)
    
  def appendleft(self, node):
    self.insertA(self.head, node)
  
  def pop(self, node = None):
    if self.size > 0:
      if not node:
        node = self.head.prev
      self.delete(node)
      return node
    else:
      raise ValueError('pop from empty double linked list')
    
  def popleft(self):
    if self.size > 0:
      node = self.head.next
      self.delete(node)
      return node
    else:
      raise ValueError('pop from empty double linked list')
  
  def display(self):
    s, node = str(self.head.val), self.head.next
    while not node == self.head:
      s += str(node.val) + "-> "
      node = node.next
    s += str(self.head.val)
    return s

class LFUCache:
  def __init__(self, capacity: int):
    # capacity
    self.capacity = capacity
    # hashmap key -> (fnode, node), O(1) get and put
    self.dict = {}
    # double linked list on freq, O(1) update and delete
    self.freq = DLinkedList()
  
  def _update(self, fnode, vnode):
    """update vnode from fnode with freq to fnode with freq + 1, create if not exists.
    """
    # create fnext with freq + 1 if not exists
    if not fnode.next == self.freq.head and fnode.next.val[0] == fnode.val[0] + 1:
      fnext = fnode.next
    else:
      fnext = Node((fnode.val[0] + 1, DLinkedList()))
      self.freq.insertA(fnode, fnext)
    # delete vnode from fnode
    fnode.val[1].pop(vnode)
    # delete fnode if empty..
    if len(fnode.val[1]) == 0:
      self.freq.pop(fnode)
    # insert vnode into fnext
    fnext.val[1].append(vnode)
    # print(f"update: {self.display()=}, ")
    return fnext, vnode

  def get(self, key: int) -> int:
    # print(f"get {key=}..")
    if key in self.dict:
      # node to hold (key, value)
      self.dict[key] = self._update(*self.dict[key])
      return self.dict[key][1].val[1]
    # print(f"get {key=}: {self.display()=}")
    return -1

  def put(self, key: int, value: int) -> None:
    # print(f"put {(key, value)=}..")
    if self.capacity > 0:
      if key in self.dict:
        # update value
        self.dict[key][1].val[1] = value
        # update fnode, vnode
        self.dict[key] = self._update(*self.dict[key])
      else:
        if len(self.dict) == self.capacity:
          minfreq_fnode = self.freq.head.next
          minfreq_vnode = minfreq_fnode.val[1].popleft()
          if len(minfreq_fnode.val[1]) == 0:
            self.freq.pop(minfreq_fnode)
          self.dict.pop(minfreq_vnode.val[0])
        # create node
        if self.freq.head.next == self.freq.head or not self.freq.head.next.val[0] == 1:
          self.freq.appendleft(Node([1, DLinkedList()]))
        fnode = self.freq.head.next
        vnode = Node([key, value])
        fnode.val[1].append(vnode)
        self.dict[key] = (fnode, vnode)
      # print(f"put {(key, value)=}: {self.display()=}")
    return None

  def display(self):
    print(f"LFUCache: {self.capacity=}")
    print(f"{len(self.dict)=}")
    for key in self.dict:
      print(f"{key=}, freq={self.dict[key][0].val[0]}, val={self.dict[key][1].val}")
    print(f"{len(self.freq)=}")
    node = self.freq.head.next
    while not node == self.freq.head:
      print(f"freq={node.val[0]}, size={len(node.val[1])}, {node.val[1].display()}")
      node = node.next
    return None

if __name__ == '__main__':
  # case 1
  lfuCache = LFUCache(capacity = 2)
  ops = ["put","put","put","put","get"]
  params = [[3,1],[2,1],[2,2],[4,4],[2]]
  # case 2
  lfuCache = LFUCache(capacity = 3)
  ops = ["put","put","get","get","get","put","put","get","get","get","get"]
  params = [[2,2],[1,1],[2],[1],[2],[3,3],[4,4],[3],[2],[1],[4]]
  # case 3
  lfuCache = LFUCache(capacity = 3)
  ops = ["put","put","put","put","get","get","get","get","put","get","get","get","get","get"]
  params = [[1,1],[2,2],[3,3],[4,4],[4],[3],[2],[1],[5,5],[1],[2],[3],[4],[5]]
  # case 4
  lfuCache = LFUCache(capacity = 10)
  ops = ["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
  params = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
  for op, param in zip(ops, params):
    if op == "put":
      print(lfuCache.put(*param))
    else:
      print(lfuCache.get(*param))
  