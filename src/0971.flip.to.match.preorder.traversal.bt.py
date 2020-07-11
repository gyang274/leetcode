from typing import List
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
    if root and voyage:
      if root.val == voyage[0]:
        if root.left and root.right:
          X = []
          if root.left.val == voyage[1]:
            pass
          elif root.right.val == voyage[1]:
            root.left, root.right = root.right, root.left
            X = [root.val]
          else:
            return [-1]
          try:
            i = voyage.index(root.right.val)
            L = self.flipMatchVoyage(root.left, voyage[1:i])
            if L == [-1]:
              return [-1]
            R = self.flipMatchVoyage(root.right, voyage[i:])
            if R == [-1]:
              return [-1]
            return X + L + R
          except ValueError as identifier:
            return [-1]
        elif root.left:
          return self.flipMatchVoyage(root.left, voyage[1:])
        elif root.right:
          return self.flipMatchVoyage(root.right, voyage[1:])
        else:
          return []
      else:
        return [-1]
    

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([1,2,3], [1,2,3]),
    ([1,2,3], [1,3,2]),
    ([1,2,3], [2,1,3]),
  ]
  cases = [
    (listToTreeNode(x), voyage) for x, voyage in cases
  ]
  rslts = [
    solver.flipMatchVoyage(root, voyage) for root, voyage in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display() if cs[0] else None}\n+{cs[1:]} | solution: {rs}")
