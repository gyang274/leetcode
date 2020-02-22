from config.listnode import ListNode, listToListNode, traverseListNode

class Solution:
  def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    if m == n: return head
    s = ListNode('')
    s.next = head
    i = 0
    x = y = z = s
    while i < m - 1:
      x = x.next
      y = y.next
      z = z.next
      i += 1
    y = y.next
    z = z.next
    i += 1
    p = x
    while i < n:
      q = z.next
      z.next = p
      p = z
      z = q
      i += 1
    x.next = z
    y.next = z.next
    z.next = p
    return s.next

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([1, 2, 3, 4, 5], 2, 4),
    ([1, 2, 3, 4, 5], 1, 1),
    ([1, 2, 3, 4, 5], 2, 2),
    ([1, 2, 3, 4, 5], 3, 4),
    ([1, 2, 3, 4, 5], 5, 5),
    ([1, 2, 3, 4, 5], 1, 5),
    ([1, 2, 3, 4, 5], 1, 4),
    ([1, 2, 3, 4, 5], 1, 5),
  ]
  cases = [
    (listToListNode(l), m, n) for l, m, n in cases
  ]
  rslts = [
    solver.reverseBetween(l, m, n) for (l, m, n) in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {traverseListNode(cs[0])} + {cs[1:]} | solution: {traverseListNode(rs)}")