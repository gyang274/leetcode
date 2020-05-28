from typing import List
from config.listnode import ListNode, listToListNode

class Solution:
  def numComponents(self, head: ListNode, G: List[int]) -> int:
    G = set(G)
    count, inside, node = 0, False, head
    while node:
      if node.val in G and not inside:
        count += 1
        inside = True
      if node.val not in G and inside:
        inside = False
      node = node.next
    return count

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([0,1,2,3,4], [0,3,1,4]),
  ]
  cases = [
    (listToListNode(l), G) for l, G in cases
  ]
  rslts = [
    solver.numComponents(head, G) for (head, G) in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs[0].display()} + {cs[1:]} | solution: {rs}")