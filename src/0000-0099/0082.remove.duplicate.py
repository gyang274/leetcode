from config.listnode import ListNode, listToListNode, traverseListNode


class Solution:
  def deleteDuplicates(self, head: ListNode) -> ListNode:
    s = ListNode('')
    s.next = head
    x = y = s
    while y and y.next:
      while y.next and y.val == y.next.val:
        y = y.next  
      y = y.next
      if (not y) or (not y.next) or (not y.val == y.next.val):
        x.next = y
        x = x.next
    return s.next


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [],
    [1],
    [1, 1],
    [1, 2],
    [1, 1, 2],
    [1, 1, 2, 3, 3, 4],
    [0, 1, 2, 2, 3, 4],
  ]
  cases = [
    listToListNode(x) for x in cases
  ]
  rslts = [
    solver.deleteDuplicates(l) for l in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {traverseListNode(cs)} | solution: {traverseListNode(rs)}")