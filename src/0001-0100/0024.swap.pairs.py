from config.listnode import ListNode, listToListNode, traverseListNode


class Solution:
  def swapPairs(self, head: ListNode) -> ListNode:
    s = ListNode(0)
    s.next = head 
    x = s
    while x.next and x.next.next:
      z = ListNode(x.next.val)
      x.next = x.next.next
      x = x.next
      z.next = x.next
      x.next = z
      x = x.next
    return s.next


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [],
    [1],
    [1, 2],
    [1, 2, 3],
    [1, 2, 3, 4],
    [1, 2, 3, 4, 5],
  ]
  cases = [
    (listToListNode(x)) for x in cases
  ]
  rslts = [
    solver.swapPairs(head) for head in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {traverseListNode(cs)} | solution: {traverseListNode(rs)}")