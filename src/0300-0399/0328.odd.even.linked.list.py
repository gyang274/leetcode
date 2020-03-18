from config.listnode import ListNode, listToListNode

class Solution:
  def oddEvenList(self, head: ListNode) -> ListNode:
    """TC: O(N), SC: O(1).
    """
    # sentinel head for odd and even
    so, se = ListNode(''), ListNode('')
    xo, xe = so, se
    while head:
      xo.next = head
      xo = xo.next
      if head.next:
        head = head.next
        xe.next = head
        xe = xe.next
      head = head.next
    xo.next = se.next
    xe.next = None
    return so.next

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [],
    [0],
    [0, 1],
    [1, 2, 3, 4, 5],
  ]
  cases = [
    listToListNode(x) for x in cases
  ]
  rslts = [
    solver.oddEvenList(head) for head in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs.display() if cs else None} | solution: {rs.display() if rs else None}")
        