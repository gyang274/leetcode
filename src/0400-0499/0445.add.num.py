from config.listnode import ListNode, listToListNode

class Solution:
  def _parse(self, l):
    x = ""
    while l:
      x += str(l.val)
      l = l.next
    return x
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    """Q0002
    """
    # parse list to str
    x1 = self._parse(l1)
    x2 = self._parse(l2)
    # add over strs
    n1 = len(x1)
    n2 = len(x2)
    # zip truncation
    if n1 < n2:
      x1 = "0" * (n2 - n1) + x1
    else:
      x2 = "0" * (n1 - n2) + x2
    # add over strs
    s = ListNode('')
    k, node = 0, s
    for i1, i2 in zip(x1[::-1], x2[::-1]):
      v = k + int(i1) + int(i2)
      k = v // 10
      v %= 10
      node.prev = ListNode(v)
      node.prev.next = node
      node = node.prev
    if k:
      node.prev = ListNode(k)
      node.prev.next = node
      node = node.prev
    # sentinel
    if node == s:
      node = None
    else:
      s.prev.next = None
    return node

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([], []),
    ([], [4]),
    ([], [1, 0]),
    ([5], [5]),
    ([5], [4, 2]),
    ([2], [9, 9, 8]),
    ([4, 2], [4, 7, 2, 3]),
    ([2, 4, 3], [5, 6, 4]),
  ]
  cases = [
    (listToListNode(x1), listToListNode(x2)) for x1, x2 in cases
  ]
  rslts = [
    solver.addTwoNumbers(l1, l2) for (l1, l2) in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs[0].display() if cs[0] else None} + {cs[1].display() if cs[1] else None} | solution: {rs.display() if rs else None}")