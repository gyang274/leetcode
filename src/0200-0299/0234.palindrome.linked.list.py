from config.listnode import ListNode, listToListNode

class Solution:
  def isPalindrome(self, head: ListNode) -> bool:
    """Two pass, 1st reach to tail and create reverse link along the way, 2nd two pointers head and tail.
      An alternative approach is 1st pass two pointers slow (1 step each iteration) and fast (2 step each iteration),
      and when fast reach to the tail, slow reach to middle, then reverse along the way slow from middle to the tail,
      and then 2nd pass two pointers head and tail and comparison along the way. 
      However, this alternative approach need more caution on corner cases, odd/even middle, empty linked list and etc.
    """
    # 1st pass
    s = ListNode('')
    s.next = head
    prev, node = s, head
    while node:
      node.prev = prev
      prev = node
      node = node.next
    t = ListNode('')
    prev.next = t
    t.prev = prev
    # 2nd pass
    x, y = s.next, t.prev
    # equality test use x is y (kind like x === y in javascript) instead of x == y, strict for reference equality,
    # because in the config.listnode, class ListNode defined __eq__() as value equal for general purpose equality.
    while not (x is y or x.prev is y):
      if not x.val == y.val:
        return False
      else:
        x = x.next
        y = y.prev
    return True

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    # [],
    [1],
    [1,2],
    [1,2,2,1],
  ]
  cases = [
    listToListNode(l) for l in cases
  ]
  rslts = [
    solver.isPalindrome(head) for head in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs.display()} | solution: {rs}")
