from config.listnode import ListNode, listToListNode

class Solution:
  def getDecimalValue(self, head: ListNode) -> int:
    node, x = head, 0
    while node:
      # x = x * 2 + node.val
      x = (x << 1) + node.val
      node = node.next
    return x

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [0],
    [1],
    [0,0],
    [0,1],
    [0,1,0],
    [0,1,1],
    [1,0,1,1],
    [1,1,0,1],
  ]
  cases = [
    listToListNode(l) for l in cases
  ]
  rslts = [solver.getDecimalValue(head) for head in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs.display()} | solution: {rs}")
