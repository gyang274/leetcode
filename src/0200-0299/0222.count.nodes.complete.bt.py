class Solution:
  def leafNodeExist(self, root: TreeNode, n: int) -> bool:
    node = root
    for x in n[1:]:
      if x == "0":
        node = node.left
      else:
        node = node.right 
    return node is not None
  def countNodes(self, root: TreeNode) -> int:
    """binary search + complete tree, use bitmask represent nodes
      e.g, 100 -> [root, left, left], keep left until leaf to define 100..0, say depth d such 0 (root depth 0), and then
      because complete, the last node is 100..0 -> 111..1, e.g. "1" + "0" * d - "1" + "1" * d, binary search by flipping
      each positions 0 to 1 until leaf is None.
    """
    if root is None:
      return 0
    # determine depth d (n's binary digits)
    n, node = ["1"], root
    while node.left is not None:
      node = node.left
      n.append("0")
    # so, n is 100..0
    for i in range(1, len(n)):
      n[i] = "1"
      if not self.leafNodeExist(root, n):
        n[i] = "0"
    return int(''.join(n), 2)
