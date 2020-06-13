from config.treenode import TreeNode, listToTreeNode

class Solution:
  def getLeafSequence(self, root):
    ans, stack = [], [root]
    while stack:
      node = stack.pop()
      if node.right or node.left:
        if node.right:
          stack.append(node.right)
        if node.left:
          stack.append(node.left)
      else:
        ans.append(node.val)
    return ans
  def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
    s1, s2 = self.getLeafSequence(root1), self.getLeafSequence(root2)
    return s1 == s2

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([1,2,3], [1,None,2,3]),
    ([3,5,1,6,2,9,8,None,None,7,4], [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]),
  ]
  cases = [
    (listToTreeNode(x1), listToTreeNode(x2)) for x1, x2 in cases
  ]
  rslts = [
    solver.leafSimilar(root1, root2) for root1, root2 in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display() if cs[0] else None}\n{cs[1].display() if cs[1] else None}\nsolution: {rs}")
