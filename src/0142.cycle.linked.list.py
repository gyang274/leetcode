from config.listnode import ListNode, listToListNode

class Solution:
  def detectCycle(self, head: ListNode) -> bool:
    """Two pointers, slow x and fast y, y move 2 step for each 1 step x move.
      if no cycle, y reach null, if cycle to from pos n to pos k, then meet at j, where 2 * (k + j) = n + j,
      e.g. x travel k + j and y travel n + j, remeber y travelled twice of x.
      so j = n - 2k, so k + j = n - k, so if z travel from head 0, x or y travel from n - k then meet at k.
    """
    x = y = head
    while y and y.next:
      x = x.next
      y = y.next.next
      if y == x:
        z = head
        while not z == x:
          x = x.next
          z = z.next
        return x
    return None