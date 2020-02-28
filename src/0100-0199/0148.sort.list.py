from config.listnode import ListNode, listToListNode

class Solution:
  def merge(self, l, x, y, r):
    """merge of two sorted linked list x, y, and connect l -> merged(x, y) -> r, move l forward to l.next = r.
    """
    while x and y:
      if x.val <= y.val:
        l.next = x
        x = x.next
      else:
        l.next = y
        y = y.next
      l = l.next
    l.next = x or y
    while l.next:
      l = l.next
    l.next = r
    return l
  def sortList(self, head: ListNode) -> ListNode:
    """merge sort on linked list.
      iterate over linked list, say, s -> head -> ...-> ..
      k: number of every k nodes are sorted, k = 1, 2, .. n, e.g., s -> l -> .. -> x -> .. -> y -> .. -> r -> .. 
                                                                                  ---------  ---------
                                                                                   k nodes    k nodes
      merge k nodes from x and y, so every 2k nodes are sorted, l and r are the left and right node for next x, y pair
    """
    s = ListNode('')
    s.next = head
    # linked list length
    # it is ok to get n from k = 1 case, but this way is more cleaner
    x, n = s, 0
    while x.next:
      x = x.next
      n += 1
    # merge sort
    k = 1
    while k < n:
      l = s
      while l.next:
        x = l.next
        # move k step forward, break link so x -> ... -> None, with lengh k
        y = x
        for _ in range(k - 1):
          if y is not None:
            y = y.next
        if y is not None:
          h = y
          y = y.next
          h.next = None
        # move k step forward, break link so y -> ... -> None, with lengh k
        r = y
        for _ in range(k - 1):
          if r is not None:
            r = r.next
        if r is not None:
          h = r
          r = r.next
          h.next = None
        # merge and connect, so that l -> mergeSorted(x, y) -> r
        if y is not None and not x == y:
          l = self.merge(l, x, y, r)
        else:
          break
      k *= 2
    return s.next

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    # [],
    [1],
    [1,2],
    [3,2],
    [4,3,1,2],
    [-1,5,3,4,0],
    [5,-1,4,3,0]
  ]
  cases = [
    listToListNode(x) for x in cases
  ]
  rslts = [
    solver.sortList(head) for head in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs.display()} | solution: {rs.display()}")