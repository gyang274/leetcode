from config.treenode import TreeNode, listToTreeNode

class Solution:
  def kthSmallest(self, root: TreeNode, k: int) -> int:
    """Key: move to smallest at leftmost, connect it's right to it's parent, k -= 1. 
      TC: O(H + k) ~= O(logN + k), SC: O(H + k) ~= O(logN + k), H is tree height which is approx O(logN).
      Follow Up: what if insert/delete + search often? maintain link from tree node to double-linked list representation 
        so that insert/delete cost O(H) on tree + O(1) on dll and search cost O(k) by following the double-linked list,
        so insert/delete + search overall is O(H+k), instead of otherwise insert/delete O(H) + search O(H+k) = O(2*H+k)
    """
    # init stack with path to smallest
    node, stack = root, []
    while node:
      stack.append(node)
      node = node.left
    while k > 0:
      hold = stack.pop()
      # push path to next smallest into stack
      node = hold.right
      while node:
        stack.append(node)
        node = node.left
      k -= 1
    return hold.val

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    # ([], 0),
    ([3,1,4,None,2], 2),
    ([5,3,6,2,4,None,None,1], 3),
  ]
  cases = [
    (listToTreeNode(x), k) for x, k in cases
  ]
  rslts = [
    solver.kthSmallest(root, k) for root, k in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display()}, {cs[1]} | solution: {rs}")  