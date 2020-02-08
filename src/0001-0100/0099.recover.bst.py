from typing import List
from config.treenode import TreeNode, listToTreeNode


class Solution:
  def recoverTree(self, root: TreeNode) -> None:
    """Do not return anything, modify root in-place instead.
      Key: inorder travel of a BST should lead to a sorted array, 
        so inorder travel and see when order is reversed then switch.
    """
    prev, last, switched = None, None, False
    if root is not None:
      node, stack = root, []
      while (node is not None or stack) and not switched:
        while node is not None:
          stack.append(node)
          node = node.left
        node = stack.pop()
        # 1st get the violation of "larger than expected"
        if prev is None and last is not None and last.val > node.val:
          prev = last
        # 2nd get the violation of "smaller than expected"
        elif prev is not None and node.val >= prev.val:
            prev.val, last.val = last.val, prev.val
            switched = True
        last = node
        node = node.right
    # inorder travel, 1st is the largest, which should be moved to last
    if not switched:
      prev.val, last.val = last.val, prev.val
    return None


class Solution:
  def recoverTree(self, root: TreeNode):
    """Do not return anything, modify root in-place instead.
      Key: inorder travel of a BST should lead to a sorted array, 
        so inorder travel and see when order is reversed then switch.
      Key: a sorted array has 1 or 2 violations of consecutive elements order,
        depends whether the switched 2 elements are consecutive or not.
        [1, 2, 3, 4, 5, 6] -> [1, 3, 2, 4, 5, 6]: 1 violations since value 2 and 3 are consecutive
        [1, 2, 3, 4, 5, 6] -> [1, 5, 3, 4, 2, 6]: 2 violations since value 2 and 5 are not consecutive
        This is corresponding to: y = root, x = prev if x is None else break.
    """
    stack = []
    x = y = prev = None  
    while stack or root:
      while root:
        stack.append(root)
        root = root.left
      root = stack.pop()
      if prev and root.val < prev.val:
        y = root
        if x is None:
          x = prev 
        else:
          break
      prev = root
      root = root.right
    x.val, y.val = y.val, x.val


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,3,None,None,2],
    [3,1,4,None,None,2],
  ]
  cases = [
    (listToTreeNode(x)) for x in cases
  ]
  rslts = [
    solver.recoverTree(x) for x in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display()}, solution: {rs}")