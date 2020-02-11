from config.listnode import ListNode, listToListNode

class Solution:
  def hasCycle(self, head: ListNode) -> bool:
    """Two pointers, slow x and fast y, y move 2 step for each 1 step x move.
      if no cycle, y reach null, if cycle to from pos n to pos k, then meet at j, where 2 * (k + j) = n + j,
      e.g. x travel k + j and y travel n + j, remeber y travelled twice of x.
    """
    x = y = head
    while y and y.next:
      x = x.next
      y = y.next.next
      if y == x:
        return True
    return False
    