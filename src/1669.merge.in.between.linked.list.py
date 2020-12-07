from config.listnode import ListNode, listToListNode

class Solution:
  def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    x, y, k = list1, list2, 0
    # move x to a-prev
    a -= 1
    while k < a:
      x = x.next
      k += 1
    # hold x, move z
    z = x
    # move z to b-next
    b += 1
    while k < b:
      z = z.next
      k += 1
    # connect a-prev -> list2 -> b-next
    x.next = y
    while y.next:
      y = y.next
    y.next = z
    return list1

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([0,1,2,3,4,5], 3, 4, [10,11,12,13,14]),
  ]
  cases = [
    (listToListNode(l1), a, b, listToListNode(l2)) for l1, a, b, l2 in cases
  ]
  rslts = [
    solver.mergeInBetween(list1, a, b, list2) for list1, a, b, list2 in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs[0].display()}, {cs[1]}, {cs[2]}, {cs[3].display()}\nsolution: {rs.display()}")
