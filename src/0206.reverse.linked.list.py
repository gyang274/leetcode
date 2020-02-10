from config.listnode import ListNode, listToListNode, traverseListNode

class Solution:
  def reverseList(self, head: ListNode) -> ListNode:
    """Recursive Solver.
    """
    if head and head.next:
      x = self.reverseList(head.next)
      head.next.next = head
      head.next = None
      return x
    else:
      return head

class Solution:
  def reverseList(self, head: ListNode) -> ListNode:
    """Iterative Solver 1.
    """
    s = ListNode(0)
    s.next = head
    if s.next and s.next.next:
      x = s.next
      y = s.next.next
      while y:
        h = s.next
        z = y.next
        s.next = y
        y.next = h
        x.next = z
        y = x.next
    return s.next

class Solution:
  def reverseList(self, head: ListNode) -> ListNode:
    """Iterative Solver 2.
    """
    prev = None
    curr = head
    while curr:
      hold = curr.next
      curr.next = prev
      prev = curr
      curr = hold
    return prev

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([]),
    ([1]),
    ([4, 2]),
    ([1, 2, 3, 4]),
  ]
  cases = [
    (listToListNode(x)) for x in cases
  ]
  rslts = [
    solver.reverseList(l) for l in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {traverseListNode(cs)} | solution: {traverseListNode(rs)}")