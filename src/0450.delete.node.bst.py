from config.treenode import TreeNode, listToTreeNode

class Solution:
  def predcessor(self, node):
    node = node.left
    while node.right:
      node = node.right
    return node.val
  def successor(self, node):
    node = node.right
    while node.left:
      node = node.left
    return node.val
  def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
    if not root:
      return None
    if root.val > key:
      root.left = self.deleteNode(root.left, key)
    elif root.val < key:
      root.right = self.deleteNode(root.right, key)
    else:
      if root.left:
        root.val = self.predcessor(root)
        root.left = self.deleteNode(root.left, root.val)
      elif root.right:
        root.val = self.successor(root)
        root.right = self.deleteNode(root.right, root.val)
      else:
        root = None
    return root
    
if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([], 0),
    ([1], 1),
    ([3,2,None,1], 2),
    ([1,None,2,None,3], 2),
    ([20,16,22,12,18,21,23,2,14,17,19,None,None,None,None,1,6,13,15,None,None,None,None,None,None,4,8,None,None,None,None,3,5,7,9,None,None,None,None,None,None,8,11], 12),
  ]
  cases = [
    (listToTreeNode(x), key) for x, key in cases
  ]
  rslts = [
    solver.deleteNode(root, key) for root, key in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display() if cs[0] else None} + {cs[1]}\nsolution:\n{rs.display() if rs else None}")