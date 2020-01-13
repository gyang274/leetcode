from typing import List


# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None


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


def listToListNode(x: List) -> ListNode:
  s = ListNode(0)
  n = s
  for v in x:
    n.next = ListNode(v)
    n = n.next
  return s.next


def traverseListNode(l: ListNode):
  s = ''
  while l:
    s += str(l.val) + ' -> '
    l = l.next
  s += 'X'
  return s


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
    print(f"case: {traverseListNode(cs[0])} + {traverseListNode(cs[1])} | solution: {traverseListNode(rs)}")