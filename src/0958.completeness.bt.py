from config.treenode import TreeNode, listToTreeNode
from collections import deque

class Solution:
  def isCompleteTree(self, root: TreeNode) -> bool:
    # level order traversal
    queue, ok = deque([root]), True
    while queue:
      node = queue.popleft()
      if ok:
        if node.left and node.right:
          queue.append(node.left)
          queue.append(node.right)
        else:
          if node.right:
            return False
          if node.left:
            queue.append(node.left)
          ok = False
      else:
        if node.left or node.right:
          return False
    return True

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,2,3,4,5,6],
    [1,2,3,4,5,None,7],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.isCompleteTree(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
