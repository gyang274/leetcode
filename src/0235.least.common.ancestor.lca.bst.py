from config.treenode import TreeNode, listToTreeNode

class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    """At each level, check p or q on the same side or not, if not then found.
    """
    node = root
    while not (node is p or node is q):
      if node.val > p.val and node.val > q.val:
        node = node.left
      elif node.val < p.val and node.val < q.val:
        node = node.right
      else:
        break
    return node

# # TODO: need a helper to put p and q as TreeNode rooted by root.
# if __name__ == '__main__':  
#   solver = Solution()
#   cases = [
#     ([6,2,8,0,4,7,9,None,None,3,5], 2, 3),
#     ([6,2,8,0,4,7,9,None,None,3,5], 3, 5),
#     ([6,2,8,0,4,7,9,None,None,3,5], 5, 8),
#     ([6,2,8,0,4,7,9,None,None,3,5], 2, 7),
#   ]
#   cases = [
#     (listToTreeNode(x), p, q) for x, p, q in cases
#   ]
#   rslts = [
#     solver.lowestCommonAncestor(root, p, q) for root, p, q in cases
#   ]
#   for cs, rs in zip(cases, rslts):
#     print(f"case:\n{cs[0].display()}, {cs[1:]} | solution: {rs}")