from collections import deque
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def findBottomLeftValue(self, root: TreeNode) -> int:
    """level order traversal
    """
    # if not root:
    #   return None
    nleft, queue, bound = root, deque([root, ]), deque([])
    while queue:
      nleft = queue[0]
      while queue:
        node = queue.popleft()
        if node.left:
          bound.append(node.left)
        if node.right:
          bound.append(node.right)
      queue, bound = bound, deque([])
    return nleft.val

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,None,2,3],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.findBottomLeftValue(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")