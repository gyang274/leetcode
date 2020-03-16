import random

class Solution:

  def __init__(self, head: ListNode):
    """@param head The linked list's head.
      Note that the head is guaranteed to be not null, so it contains at least one node.
    """
    self.list = []
    while head:
      self.list.append(head.val)
      head = head.next

  def getRandom(self) -> int:
    """Returns a random node's value.
    """
    return random.choice(self.list)

# NOTE: reservoir sampling if linked list extremely large.