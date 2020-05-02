class ListNode:
  
  def __init__(self, x):
    self.val = x
    self.next = None
    self.prev = None

class MyLinkedList:

  def __init__(self):
    """Initialize your data structure here.
    """
    self.head = ListNode('')
    self.tail = ListNode('')
    self.head.next = self.tail
    self.tail.prev = self.head
    
  def get(self, index: int) -> int:
    """Get the value of the index-th node in the linked list. If the index is invalid, return -1.
    """
    i, curr = -1, self.head
    while i < index and not curr.next == self.tail:
      curr = curr.next
      i += 1
    return curr.val if i == index else -1

  def addAtHead(self, val: int) -> None:
    """Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
    """
    node = ListNode(val)
    hold = self.head.next
    self.head.next = node
    node.prev = self.head
    node.next = hold
    hold.prev = node

  def addAtTail(self, val: int) -> None:
    """Append a node of value val to the last element of the linked list.
    """
    node = ListNode(val)
    hold = self.tail.prev
    self.tail.prev = node
    node.next = self.tail
    node.prev = hold
    hold.next = node
    
  def addAtIndex(self, index: int, val: int) -> None:
    """Add a node of value val before the index-th node in the linked list. 
      If index equals to the length of linked list, the node will be appended to the end of linked list. 
      If index is greater than the length, the node will not be inserted.
    """
    i, curr = 0, self.head
    while i < index and not curr.next == self.tail:
      curr = curr.next
      i += 1
    if i == index:
      node = ListNode(val)
      hold = curr.next
      curr.next = node
      node.prev = curr
      node.next = hold
      hold.prev = node

  def deleteAtIndex(self, index: int) -> None:
    """Delete the index-th node in the linked list, if the index is valid.
    """
    i, curr = -1, self.head
    while i < index and not curr.next == self.tail:
      curr = curr.next
      i += 1
    if i == index:
      curr.prev.next = curr.next
      curr.next.prev = curr.prev

class ListNode:

  def __init__(self, x):
    self.val = x
    self.next = None
    self.prev = None

class MyLinkedList:

  def __init__(self):
    """Initialize your data structure here.
    """
    self.size = 0
    self.head = ListNode('')
    self.tail = ListNode('')
    self.head.next = self.tail
    self.tail.prev = self.head
    
  def get(self, index: int) -> int:
    """Get the value of the index-th node in the linked list. If the index is invalid, return -1.
    """
    if index < 0 or index >= self.size:
      return -1
    if index < self.size - index:
      node = self.head
      for _ in range(index + 1):
        node = node.next
    else:
      node = self.tail
      for _ in range(self.size - index):
        node = node.prev
    return node.val

  def addAtHead(self, val: int) -> None:
    """Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
    """
    node = ListNode(val)
    hold = self.head.next
    self.head.next = node
    node.prev = self.head
    node.next = hold
    hold.prev = node
    self.size += 1

  def addAtTail(self, val: int) -> None:
    """Append a node of value val to the last element of the linked list.
    """
    node = ListNode(val)
    hold = self.tail.prev
    self.tail.prev = node
    node.next = self.tail
    node.prev = hold
    hold.next = node
    self.size += 1
    
  def addAtIndex(self, index: int, val: int) -> None:
    """Add a node of value val before the index-th node in the linked list. 
      If index equals to the length of linked list, the node will be appended to the end of linked list. 
      If index is greater than the length, the node will not be inserted.
    """
    if 0 <= index <= self.size:
      node = ListNode(val)
      if index < self.size - index:
        curr = self.head
        for _ in range(index):
          curr = curr.next
        hold = curr.next
        curr.next = node
        node.prev = curr
        node.next = hold
        hold.prev = node
      else:
        curr = self.tail
        for _ in range(self.size - index):
          curr = curr.prev
        hold = curr.prev
        curr.prev = node
        node.next = curr
        node.prev = hold
        hold.next = node
      self.size += 1

  def deleteAtIndex(self, index: int) -> None:
    """Delete the index-th node in the linked list, if the index is valid.
    """
    if 0 <= index < self.size:
      if index < self.size - index:
        curr = self.head
        for _ in range(index + 1):
          curr = curr.next
      else:
        curr = self.tail
        for _ in range(self.size - index):
          curr = curr.prev
      curr.prev.next = curr.next
      curr.next.prev = curr.prev
      self.size -= 1
