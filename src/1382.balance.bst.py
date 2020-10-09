from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, x):
    n = len(x)
    i = n // 2
    node = TreeNode(x[i])
    if n > 1:
      node.left = self.recursive(x[:i])
    if n > 2:
      node.right = self.recursive(x[(i + 1):])
    return node
  def balanceBST(self, root: TreeNode) -> TreeNode:
    # inorder traversal bst => sorted list
    x = []
    if root:
      node, stack = root, []
      while node or stack:
        while node:
          stack.append(node)
          node = node.left
        node= stack.pop()
        x.append(node.val)
        node = node.right
    # build balanced BST
    return self.recursive(x)

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,None,3,2],
    [1,None,2,None,3,None,4,None,None]
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.balanceBST(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None}\nsolution:\n{rs.display() if rs else None} ")
