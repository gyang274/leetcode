from typing import List
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def inorderTraversal(self, root: TreeNode) -> List[int]:
    x = []
    if root is not None:
      node, stack = root, []
      while node or stack:
        while node is not None:
          stack.append(node)
          node = node.left
        node = stack.pop()
        x.append(node.val)
        node = node.right
    return x
  def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
    # merge 2 sorted list in O(N)
    arr1, arr2 = self.inorderTraversal(root1), self.inorderTraversal(root2)
    ans, i1, i2, n1, n2 = [], 0, 0, len(arr1), len(arr2)
    while i1 < n1 or i2 < n2:
      if (i1 < n1 and i2 < n2 and arr1[i1] <= arr2[i2]) or i2 == n2:
        ans.append(arr1[i1])
        i1 += 1
      else:
        ans.append(arr2[i2])
        i2 += 1
    return ans

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([2,1,4], [1,0,3]),
  ]
  cases = [
    (listToTreeNode(x), listToTreeNode(y)) for x, y in cases
  ]
  rslts = [
    solver.getAllElements(root1, root2) for root1, root2 in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display() if cs else None}\n{cs[1].display() if cs else None}\nsolution: {rs}")
