from config.listnode import ListNode, listToListNode

class Solution:
  def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
    s = ListNode('')
    s.next = head
    prev, node = s, head
    while node:
      count = 0
      while node and count < m:
        prev, node = node, node.next
        count += 1
      hold = prev
      if count == m:
        count = 0
        while node and count < n:
          prev, node = node, node.next
          count += 1
      prev = hold
      # passthrough
      prev.next = node
    return s.next

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([1,2,3,4,5,6,7,8,9,10,11,12,13,14], 2, 3),
    ([1,2,3,4,5,6,7,8,9,10,11,12,13,14], 1, 4),
    ([1,2,3,4,5,6,7,8,9,10,11,12,13,14], 4, 2),
  ]
  cases = [
    (listToListNode(l), m,n) for l, m, n in cases
  ]
  rslts = [
    solver.deleteNodes(head, m, n) for head, m, n in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs[0].display()} + {cs[1:]} | solution: {rs.display()}")