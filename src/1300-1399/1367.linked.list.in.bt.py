from collections import deque
from config.listnode import ListNode, listToListNode
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
    q = deque([(root, [head])])
    while q:
      # x, ys: tree node, candidate list nodes
      x, ys = q.popleft()
      zs = []
      for y in ys:
        if y.val == x.val:
          if not y.next:
            return True
          zs.append(y.next)
      if x.left:
        q.append((x.left, zs + [head]))
      if x.right:
        q.append((x.right, zs + [head]))
    return False

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([4,2,8], [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3]),
    ([1,4,2,6], [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3]),
    ([1,4,2,6,8], [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3]),
  ]
  cases = [
    (listToListNode(x), listToTreeNode(y)) for x, y in cases
  ]
  rslts = [
    solver.isSubPath(head, root) for head, root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display() if cs[0] else None}\n{cs[1].display() if cs[1] else None}\nsolution: {rs}")
