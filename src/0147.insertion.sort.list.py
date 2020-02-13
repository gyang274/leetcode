from config.listnode import ListNode, listToListNode

class Solution:
  def insertionSortList(self, head: ListNode) -> ListNode:
    # INTEGER_MIN
    s = ListNode(-2147483648)
    s.next = head
    # insertion sort
    x = head
    while x and x.next:
      y = x.next
      if y.val < x.val:
        z = s
        while not z == x:
          if y.val < z.next.val:
            x.next = y.next
            y.next = z.next
            z.next = y
            break
          z = z.next
      else:
        x = x.next
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
  ]
  cases = [
    listToListNode(x) for x in cases
  ]
  rslts = [
    solver.insertionSortList(head) for head in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs.display()} | solution: {rs.display()}")