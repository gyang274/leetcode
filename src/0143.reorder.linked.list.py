from config.listnode import ListNode, listToListNode

class Solution:
  def reorderList(self, head: ListNode) -> None:
    """Do not return anything, modify head in-place instead.
    """
    s = ListNode('')
    s.next = head
    # step 1: reverse the 2nd half of the linked list: 1->2->3->4->5 to 1->2->3<-4<-5
    x = y = s
    while y:
      x = x.next
      y = y.next
      if y:
        y = y.next
    # x is the middle one, reverse from x to ende
    prev, curr = None, x
    while curr:
      hold = curr.next
      curr.next = prev
      prev = curr
      curr = hold
    # step 2: two pointers from init and ende to switch 1(x)->2->3<-4<-5(y) to 1->5->2(x)->3<-4(y) to 1->5->2->4->3
    x, y = head, prev
    while not (x == y or x.next == y):
      # hold of x.next and y.next
      u, v = x.next, y.next
      x.next = y
      y.next = u
      x, y = u, v
    return None

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    # [],
    [1],
    [1,2],
    [1,2,3],
    [1,2,3,4],
    [1,2,3,4,5],
  ]
  cases = [
    listToListNode(x) for x in cases
  ]
  rslts = [
    solver.reorderList(head) for head in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs.display()} | solution: {rs}")
