from typing import List
from config.treenode import TreeNode, listToTreeNode


class Solution:
  def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    if root is None:
      return []
    i, stack, holds, x = -1, [], [root, ], []
    while stack or holds:
      if stack:
        node = stack.pop()
        x[i].append(node.val)
        if i % 2 == 0:
          if node.left is not None:
            holds.append(node.left)
          if node.right is not None:
            holds.append(node.right)
        else:
          if node.right is not None:
            holds.append(node.right)
          if node.left is not None:
            holds.append(node.left)
      else:
        stack, holds = holds, []
        i += 1
        x.append([])
    return x


class Solution:
  def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    if root is None:
      return []
    i, stack, holds, x = 0, [root, ], [], [[], ]
    while stack or holds:
      if stack:
        node = stack.pop()
        x[i].append(node.val)
        if i % 2 == 0:
          if node.left is not None:
            holds.append(node.left)
          if node.right is not None:
            holds.append(node.right)
        else:
          if node.right is not None:
            holds.append(node.right)
          if node.left is not None:
            holds.append(node.left)
      else:
        stack, holds = holds, []
        i += 1
        x.append([])
    return x


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    # [],
    [1, None, 2, 3],
    [1,2,3,4,None,None,5],
    [3,9,20,None,None,15,7],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.zigzagLevelOrder(x) for x in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display()}, solution: {rs}")

