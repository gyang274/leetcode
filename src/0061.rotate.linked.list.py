from config.listnode import ListNode, listToListNode, traverseListNode


class Solution:
  def rotateRight(self, head: ListNode, k: int) -> ListNode:
    """Two pointers.
    """
    s = ListNode(0)
    s.next = head
    if not s.next:
      return s.next
    x, y, i = s, s, 0
    while i < k:
      if y.next:
        y = y.next
      else:
        y = s.next
        k %= i
        if k == 0:
          k += i * 2
        else:
          k += i
      i += 1
    while y.next:
      x = x.next
      y = y.next
    if not x == s:
      y.next = s.next
      s.next = x.next
      x.next = None
    return s.next


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    # ([1, 2, 3, 4, 5], 2),
    # ([0, 1, 2], 3),
    # ([0, 1, 2], 4),
    # ([0, 1, 2], 1),
    # ([], 0),
    # ([], 1),
    # ([], 2),
    # ([1], 0),
    # ([1], 1),
    # ([1], 2),
    # ([1, 2], 2),
    ([1, 2, 3], 3),
    ([1,2,3], 2000000000),
    ([1,2,3,4,5], 10),
  ]
  cases = [
    (listToListNode(x), k) for x, k in cases
  ]
  rslts = [
    solver.rotateRight(h, k) for (h, k) in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {traverseListNode(cs[0])} + {cs[1]} | solution: {traverseListNode(rs)}")   