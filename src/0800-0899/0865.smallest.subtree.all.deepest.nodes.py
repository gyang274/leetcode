from config.treenode import TreeNode, listToTreeNode

class Solution:
  def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
    # preorder traversal, assign depth
    root.depth = 0
    stack, dmax, dmaxNodes = [root], 0, {root}
    while stack:
      node = stack.pop()
      if node.right:
        node.right.parent = node
        node.right.depth = node.depth + 1
        if node.right.depth > dmax:
          dmax = node.right.depth
          dmaxNodes = {node.right}
        elif node.right.depth == dmax:
          dmaxNodes.add(node.right)
        stack.append(node.right)
      if node.left:
        node.left.parent = node
        node.left.depth = node.depth + 1
        if node.left.depth > dmax:
          dmax = node.left.depth
          dmaxNodes = {node.left}
        elif node.left.depth == dmax:
          dmaxNodes.add(node.left)
        stack.append(node.left)
    # climb back to common ancestor
    while len(dmaxNodes) > 1:
      dmaxNodes = set(node.parent for node in dmaxNodes)
    return dmaxNodes.pop()

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,None,2,3],
    [3,5,1,6,2,0,8,None,None,7,4]
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.subtreeWithAllDeepest(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None}\nsolution:\n{rs.display() if rs else None}")
