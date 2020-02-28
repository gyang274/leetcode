from typing import List
from collections import deque
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def rightSideView(self, root: TreeNode) -> List[int]:
    """BFS, level order traversal, keep the last node value of each level.
      collections.deque support constant time append/pop from both head and tail, whereas list can cost up to O(n) 
      when pop from left, e.g., list.pop(0).
    """
    views = []
    if root is not None:
      # stack, holds = [], [root, ]
      stack, holds = deque([]), deque([root, ])
      while stack or holds:
        while stack:
          # node = stack.pop(0)
          node = stack.popleft()
          if node.left is not None:
            holds.append(node.left)
          if node.right is not None:
            holds.append(node.right)
        stack, holds = holds, deque([])
        if stack:
          views.append(stack[-1].val)
    return views

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    # [],
    [1, None, 2, 3],
    [3,9,20,None,None,15,7],
    [1,2,3,None,5,None,4,9],
  ]
  cases = [
    (listToTreeNode(x)) for x in cases
  ]
  rslts = [
    solver.rightSideView(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display()}, solution: {rs}")
