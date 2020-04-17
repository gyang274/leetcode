from config.treenode import TreeNode, listToTreeNode

class Solution:
  def convertBST(self, root: TreeNode) -> TreeNode:
    if not root:
      return None
    x = []
    node, stack = root, []
    while node or stack:
      while node:
        stack.append(node)
        node = node.left
      node = stack.pop()
      x.append(node)
      node = node.right
    for i in range(len(x) - 2, -1, -1):
      x[i].val += x[i + 1].val
    return root

class Solution:
  def convertBST(self, root: TreeNode) -> TreeNode:
    if not root:
      return None
    prev, node, stack = 0, root, []
    while node or stack:
      while node:
        stack.append(node)
        node = node.right
      node = stack.pop()
      node.val += prev
      prev = node.val
      node = node.left
    return root

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    # [1,None,3,2],
    [5, 2, 13]
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.convertBST(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution:\n{rs.display() if rs else None}")
