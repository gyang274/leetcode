from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node):
    # postorder traversal
    # excess coins from left
    L = self.recursive(node.left) if node.left else 0
    # excess coins from right
    R = self.recursive(node.right) if node.right else 0
    # moves to this node
    self.moves += abs(L) + abs(R)
    # excess coins out from this node 
    # and moves are counted in parent
    return node.val + L + R - 1
  def distributeCoins(self, root: TreeNode) -> int:
    self.moves = 0
    self.recursive(root)
    return self.moves

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [3,0,0],
    [0,3,0],
    [1,0,2],
    [1,0,0,None,3],
    [0,1,None,3,0],
    [0,1,1,0,3,None,2,None,None,0],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.distributeCoins(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
