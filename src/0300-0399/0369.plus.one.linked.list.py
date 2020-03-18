from config.listnode import ListNode, listToListNode

class Solution:
  def plusOne(self, head: ListNode) -> ListNode:
    # sentinel node
    s = ListNode('')
    s.next = head
    # create prev along the way
    node = s
    while node.next:
      node.next.prev = node
      node = node.next
    # plus one on the node from tail
    while True:
      if node.val < 9:
        node.val += 1
        break
      else:
        node.val = 0
        node = node.prev
        if node.val == '':
          x = ListNode(1)
          x.next = node.next
          node.next.prev = x
          node.next = x
          x.prev = node
          break
    return s.next

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [0],
    [1],
    [9],
    [4,2],
    [4,2,9,8],
    [4,2,9,9],
    [9,9,9,9],
  ]
  cases = [
    listToListNode(l) for l in cases
  ]
  rslts = [
    solver.plusOne(head) for head in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs.display() if cs else None} | solution: {rs.display() if rs else None}")