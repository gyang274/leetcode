from typing import List
from collections import deque
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def largestValues(self, root: TreeNode) -> List[int]:
    """level order traversal
    """
    if not root:
      return []
    ans, queue, value, bound = [], deque([root, ]), [root.val, ], deque([])
    while queue:
      ans.append(max(value))
      value = []
      while queue:
        node = queue.popleft()
        if node.left:
          bound.append(node.left)
          value.append(node.left.val)
        if node.right:
          bound.append(node.right)
          value.append(node.right.val)
      queue, bound = bound, deque([])
    return ans

class Solution:
  def largestValues(self, root: TreeNode) -> List[int]:
    """level order traversal
    """
    if not root:
      return []
    ans, queue, value, bound = [], deque([root, ]), [root.val, ], deque([])
    while queue:
      ans.append(max(value))
      value = []
      for node in queue:
        if node.left:
          bound.append(node.left)
          value.append(node.left.val)
        if node.right:
          bound.append(node.right)
          value.append(node.right.val)
      queue, bound = bound, deque([])
    return ans

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,None,2,3],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.largestValues(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
