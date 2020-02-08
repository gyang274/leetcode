from config.listnode import ListNode, listToListNode, traverseListNode




class Solution:
  def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    """Keep Two Pairs, prev and curr, prev group tail and curr group head.
    """
    s = prevK = ListNode(0)
    s.next = holdK = currK = head
    i = 1
    while currK:
      currK = currK.next
      if i % k == 0:
        prev, curr = currK, holdK
        for _ in range(k):
          curr.next, curr, prev = prev, curr.next, curr
        prevK.next, prevK, holdK = prev, holdK, currK
      i += 1
    return s.next


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([], 2),
    ([1], 1),
    ([1], 2),
    ([4, 2], 1),
    ([4, 2], 2),
    ([1, 2, 3, 4], 1),
    ([1, 2, 3, 4], 2),
    ([1, 2, 3, 4], 3),
    ([1, 2, 3, 4, 5, 6, 7, 8], 1),
    ([1, 2, 3, 4, 5, 6, 7, 8], 2),
    ([1, 2, 3, 4, 5, 6, 7], 3),
  ]
  cases = [
    (listToListNode(x), k) for x, k in cases
  ]
  rslts = [
    solver.reverseKGroup(l, k) for l, k in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {traverseListNode(cs[0])} - {cs[1]} | solution: {traverseListNode(rs)}")