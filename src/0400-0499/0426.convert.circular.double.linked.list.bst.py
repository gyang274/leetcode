from config.treenode import TreeNode, listToTreeNode

class Solution:
  def treeToDoublyList(self, root: TreeNode) -> TreeNode:
    # sentinel
    s = TreeNode('')
    # inorder traversal
    x = s
    if root:
      node, stack = root, []
      while node or stack:
        while node:
          stack.append(node)
          node = node.left
        # next smallest
        node = stack.pop()
        # create the double link in-place
        x.right = node
        node.left = x
        # move along the path of double linked list
        x = node
        # move along the path of tree inorder traversal
        node = node.right
      # complete the circle
      x.right = s.right
      s.right.left = x
    return s.right

# if __name__ == '__main__':  
#   solver = Solution()
#   cases = [
#     [],
#     [1],
#     [2,1,3],
#     [4,2,5,1,3],
#   ]
#   cases = [
#     listToTreeNode(x) for x in cases
#   ]
#   rslts = [
#     solver.treeToDoublyList(root) for root in cases
#   ]
#   for cs, rs in zip(cases, rslts):
#     print(f"case:\n{cs.display() if cs else None} | solution: {rs}")