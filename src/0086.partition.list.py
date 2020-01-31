from config.listnode import ListNode, listToListNode, traverseListNode


class Solution:
  def partition(self, head: ListNode, x: int) -> ListNode:
    p = l = ListNode('') 
    q = g = ListNode('')
    z = head
    while z:
      if z.val < x:
        l.next = z
        l = l.next
      else:
        g.next = z
        g = g.next
      z = z.next
    l.next = q.next
    g.next = None
    return p.next


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([], 0),
    ([1], 0),
    ([1, 1], 1),
    ([1, 3, 2], 3),
    ([1, 3, 2], 2),
    ([1, 4, 3, 2, 5, 2], 3),
  ]
  cases = [
    (listToListNode(l), x) for l, x in cases
  ]
  rslts = [
    solver.partition(l, x) for l, x in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {traverseListNode(cs[0])} - {cs[1]} | solution: {traverseListNode(rs)}")