"""Definition for a Node.
class Node:
  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next
"""

class Solution:
  def insert(self, head: 'Node', insertVal: int) -> 'Node':
    node = Node(insertVal)
    if not head:
      node.next = node
      return node
    prev, curr = head, head.next
    while True:
      if (prev.val < insertVal <= curr.val) or (prev.val > curr.val and (insertVal >= prev.val or insertVal <= curr.val)):
        prev.next = node
        node.next = curr
        return head
      prev, curr = curr, curr.next
      if prev == head:
        break
    # all equal value in circle
    prev.next = node
    node.next = curr
    return head
