from config.listnode import List, ListNode, listToListNode, traverseListNode


class Solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    s = ListNode(0)
    s.next = head
    x = s
    z = s
    for i in range(n):
      x = x.next
    while x.next:
      x = x.next
      z = z.next
    z.next = z.next.next
    return s.next


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ([1], 1),
    ([1, 2, 3, 4, 5], 1),
    ([1, 2, 3, 4, 5], 4),
    ([1, 2, 3, 4, 5], 2),
  ]
  cases = [
    (listToListNode(head), n) for head, n in cases
  ]
  rslts = [solver.removeNthFromEnd(head, n) for head, n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {traverseListNode(cs[0])}, {cs[1]} | solution: {traverseListNode(rs)}")