from typing import List
from config.listnode import ListNode, listToListNode

class Solution:
  def nextLargerNodes(self, head: ListNode) -> List[int]:
    node, i, stack, ans = head, 0, [], []
    while node:
      while stack and stack[-1][1] < node.val:
        ans[stack.pop()[0]] = node.val
      stack.append((i, node.val))
      ans.append(0)
      node = node.next
      i += 1
    return ans

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [2,8,5,7,1,4],
    [2,7,1,4,5,8],
  ]
  cases = [
    listToListNode(l) for l in cases
  ]
  rslts = [
    solver.nextLargerNodes(head) for head in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs.display() if cs else None} | solution: {rs}")