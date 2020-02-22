from config.listnode import ListNode, listToListNode

class Solution:
  def removeElements(self, head: ListNode, val: int) -> ListNode:
    s = ListNode('')
    s.next = head
    prev, node = s, head
    while node:
      if node.val == val:
        # skip node, hold prev
        prev.next = node.next
      else:
        # move prev to forward
        prev = node
      node = node.next
    return s.next

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([], 0),
    ([1], 1),
    ([1, 1], 1),
    ([1, 4, 2], 4),
    ([1, 4, 2], 2),
  ]
  cases = [
    (listToListNode(l), val) for l, val in cases
  ]
  rslts = [
    solver.removeElements(head, val) for head, val in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs[0].display()} + {cs[1:]} | solution: {rs.display()}")