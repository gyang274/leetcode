from config.treenode import TreeNode, listToTreeNode

class Solution:
  def closestValue(self, root: TreeNode, target: float) -> int:
    """modified binary search, some node and its largest left children, or some node or its smallest right children.
      TC: O(H), SC: O(1), H is the tree height, ~O(logN).
    """
    node, x, dmin = root, None, float('inf')
    while node:
      if target == node.val:
        return node.val
      elif target < node.val:
        if node.val - target < dmin:
          x, dmin = node.val, node.val - target
        node = node.left
      else:
        if target - node.val < dmin:
          x, dmin = node.val, target - node.val
        node = node.right
    return x

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([0], 2147483648.0),
    ([4,2,7,1,3,5,8], 3.72),
    ([4,2,7,1,3,5,8], 3.14),
    ([4,2,7,1,3,5,8], 5.14),
    ([4,2,7,1,3,5,8], 5.98),
    ([4,2,7,1,3,5,8], 6.18),
    ([4,2,7,1,3,5,8], 7.12),
  ]
  cases = [
    (listToTreeNode(x), target) for x, target in cases
  ]
  rslts = [
    solver.closestValue(root, target) for root, target in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display()}, {cs[1]} | solution: {rs}")          