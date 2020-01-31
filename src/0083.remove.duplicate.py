from config.listnode import ListNode, listToListNode, traverseListNode


class Solution:
  def deleteDuplicates(self, head: ListNode) -> ListNode:
    s = ListNode(0)
    s.next = head
    x = y = head
    while y and y.next:
      y = y.next
      if x.val < y.val:
        x.next = y
        x = x.next
    if x and x.next:
      x.next = None
    return s.next


class Solution:
  def deleteDuplicates(self, head: ListNode) -> ListNode:
    x = head
    while x and x.next:
      if x.val == x.next.val:
        x.next = x.next.next
      else:
        x = x.next
    return head


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [],
    [1],
    [1, 1],
    [1, 2],
    [1, 1, 2],
    [1, 1, 2, 3, 3, 4],
  ]
  cases = [
    listToListNode(x) for x in cases
  ]
  rslts = [
    solver.deleteDuplicates(l) for l in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {traverseListNode(cs)} | solution: {traverseListNode(rs)}")