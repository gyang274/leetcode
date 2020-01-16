from config.listnode import ListNode, listToListNode, traverseListNode


class Solution:
  def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    s = l = ListNode(0)
    while l1 and l2:
      if l1.val <= l2.val:
        l.next = ListNode(l1.val)
        l1 = l1.next
      else:
        l.next = ListNode(l2.val)
        l2 = l2.next
      l = l.next
    l.next = l1 or l2
    return s.next


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([1, 2, 4], [1, 3, 4]),
    ([2, 3], [0, 1, 1, 4]),
    ([5], [5]),
    ([], []),
    ([], [4]),
    ([], [0, 1])
  ]
  cases = [
    (listToListNode(x1), listToListNode(x2)) for x1, x2 in cases
  ]
  rslts = [
    solver.mergeTwoLists(l1, l2) for (l1, l2) in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {traverseListNode(cs[0])} + {traverseListNode(cs[1])} | solution: {traverseListNode(rs)}")