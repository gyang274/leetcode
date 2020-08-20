from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, node):
    # determine the num of nodes on left subtree and right subtree
    nl = 0
    if node.left:
      nl = self.recursive(node.left)
    nr = 0
    if node.right:
      nr = self.recursive(node.right)
    # if 1st player choose left/right child, by taking this parent node, how many blocked?
    if node.left and node.left.val == self.x:
      self.counts[2] = self.n - nl
    if node.right and node.right.val == self.x:
      self.counts[2] = self.n - nr
    # if 1st player choose this parent node, by taking left/right child, how many blocked?
    if node.val == self.x:
      self.counts[:2] = (nr, nl)
    return nr + nl + 1
  def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
    # choose between (nodeX-left-child, nodeX-right-child, nodeX-parent), count and determine
    self.counts, self.n, self.x = [0, 0, 0], n, x
    self.recursive(root)
    return max(self.counts) > n // 2

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([1,None,2,3], 3, 1),
    ([1,None,2,3], 3, 2),
    ([1,None,2,3], 3, 3),
    ([1,2,3,4,5,6,7,8,9,10,11], 11, 1),
    ([1,2,3,4,5,6,7,8,9,10,11], 11, 2),
    ([1,2,3,4,5,6,7,8,9,10,11], 11, 3),
  ]
  cases = [
    (listToTreeNode(r), n, x) for r, n, x in cases
  ]
  rslts = [
    solver.btreeGameWinningMove(root, n, x) for root, n, x in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display() if cs else None} + {cs[1:]} | solution: {rs}")
