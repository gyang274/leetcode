from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node):
    self.count[node.val - 1] += 1
    if node.left or node.right:
      if node.left:
        self.recursive(node.left)
      if node.right:
        self.recursive(node.right)
    else:
      if sum(map(lambda x: x & 1, self.count)) <= 1:
        self.p += 1
    self.count[node.val - 1] -= 1
  def pseudoPalindromicPaths (self, root: TreeNode) -> int:
    self.count, self.p = [0] * 9, 0
    self.recursive(root)
    return self.p

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [2,3,1,3,1,None,1],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.pseudoPalindromicPaths(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
