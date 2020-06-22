from config.listnode import ListNode, listToListNode

class Solution:
  def middleNode(self, head: ListNode) -> ListNode:
    x, y = head, head
    while y:
      y = y.next
      if y:
        y = y.next
        x = x.next
    return x

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,2,3,4,5],
    [1,2,3,4,5,6,7,8],
  ]
  cases = [
    listToListNode(l) for l in cases
  ]
  rslts = [
    solver.middleNode(head) for head in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs.display() if cs else None} | solution: {rs.display() if rs else None}")