from typing import List
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
    if not root:
      return None, None
    elif root.val > V:
      if not root.left:
        node = None
      else:
        node, root.left = self.splitBST(root.left, V)
      return node, root
    else:
      if not root.right:
        node = None
      else:
        root.right, node = self.splitBST(root.right, V)
      return root, node

class Solution:
  def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
    if not root:
      return None, None
    elif root.val > V:
      node, root.left = self.splitBST(root.left, V)
      return node, root
    else:
      root.right, node = self.splitBST(root.right, V)
      return root, node

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([4,2,6,1,3,5,7], 1),
    ([4,2,6,1,3,5,7], 2),
    ([4,2,6,1,3,5,7], 3),
    ([4,2,6,1,3,5,7], 4),
    ([4,2,6,1,3,5,7], 5),
    ([4,2,6,1,3,5,7], 6),
    ([4,2,6,1,3,5,7], 7),
  ]
  cases = [
    (listToTreeNode(x), V) for x, V in cases
  ]
  rslts = [
    solver.splitBST(root, V) for root, V in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display() if cs else None} + {cs[1:]} |\nsolution:\n{rs[0].display() if rs[0] else None}\n{rs[1].display() if rs[1] else None}")
