from config.treenode import TreeNode, listToTreeNode

class Solution:
  def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
    if d == 1:
      node = TreeNode(v)
      node.left = root
      return node
    # level order traversal
    if root:
      level, stack = 0, [root]
      while stack:
        level, queue = level + 1, []
        if level == d - 1:
          for node in stack:
            xl, xr = TreeNode(v), TreeNode(v)
            xl.left, xr.right = node.left, node.right
            node.left, node.right = xl, xr
          break
        else:
          for node in stack:
            if node.left:
              queue.append(node.left)
            if node.right:
              queue.append(node.right)
          stack = queue
    return root

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([1,None,2,3], 1, 1),
    ([1,None,2,3], 1, 2),
  ]
  cases = [
    (listToTreeNode(x), v, d) for x, v, d in cases
  ]
  rslts = [
    solver.addOneRow(root, v, d) for root, v, d in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display() if cs[0] else None}, {cs[1:]} | solution:\n{rs.display() if rs else None}")
