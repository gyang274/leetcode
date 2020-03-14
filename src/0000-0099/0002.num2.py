from config.listnode import ListNode, listToListNode

class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    n = s = ListNode(0)
    k = 0
    while l1 or l2 or k > 0:
      if l1:
        k += l1.val
        l1 = l1.next
      if l2:
        k += l2.val
        l2 = l2.next
      n.next = ListNode(k % 10)
      k //= 10
      n = n.next
    return s.next

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([2, 4, 3], [5, 6, 4]),
    ([4, 2], [4, 7, 2, 3]),
    ([5], [5]),
    ([], []),
    ([], [4]),
    ([], [0, 1])
  ]
  cases = [
    (listToListNode(x1), listToListNode(x2)) for x1, x2 in cases
  ]
  rslts = [
    solver.addTwoNumbers(l1, l2) for (l1, l2) in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs[0].display()} + {cs[1].display()} | solution: {rs.display()}")