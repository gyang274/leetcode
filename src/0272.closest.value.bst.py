from typing import List
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
    """TC: O(k) partial inorder travel to get until >= target, then expand on both side stop when k fulfilled.
      Worst case O(N).
    """
    return None

class Solution:
  def _nextLT(self, stack):
    """find node with largest value < stack[-1].val.
    """
    if stack:
      node = stack.pop()
      # partial inorder: (left, root, right)
      if node.left:
        node = node.left
        stack.append(node)
        while node.right:
          node = node.right
          stack.append(node)
      else:
        while stack and stack[-1].val > node.val:
          stack.pop()
      return stack[-1].val if stack else None
    return None
  def _nextGT(self, stack):
    """find node with smallest value > stack[-1].val.
    """
    if stack:
      node = stack.pop()
      # partial inorder: (left, root, right)
      if node.right:
        node = node.right
        stack.append(node)
        while node.left:
          node = node.left
          stack.append(node)
      else:
        while stack and stack[-1].val < node.val:
          stack.pop()
      return stack[-1].val if stack else None
    return None
  def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
    """maintain 2 stacks, 1st keep find next largest < target, 2nd keep find next smallest > target.
    """
    # init stack as path to closest as in Q270, assume k >= 1.
    node, x, dmin, stack = root, None, float('inf'), []
    while node:
      stack.append(node)
      if target == node.val:
        x, dmin = node.val, 0
        break
      elif target < node.val:
        if node.val - target < dmin:
          x, dmin = node.val, node.val - target
        node = node.left
      else:
        if target - node.val < dmin:
          x, dmin = node.val, target - node.val
        node = node.right
    # reinstate stack to path from root to closest
    while not stack[-1].val == x:
      stack.pop()
    # ans keep 1st, .., kth closest to target
    ans, i = [stack[-1].val, ], 1
    # stack1 keeps < _pseudo_target, 2nd keep > _pseudo_target (node.val of closest)
    stack1, stack2 = stack.copy(), stack.copy()
    self._nextLT(stack1)
    self._nextGT(stack2)
    while i < k:
      if stack1 and stack2:
        if abs(stack1[-1].val - target) < abs(stack2[-1].val - target):
          ans.append(stack1[-1].val)
          self._nextLT(stack1)
        else:
          ans.append(stack2[-1].val)
          self._nextGT(stack2)
      elif stack1:
        ans.append(stack1[-1].val)
        self._nextLT(stack1)
      else:
        ans.append(stack2[-1].val)
        self._nextGT(stack2)
      i += 1
    return ans

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([0], 2147483648.0, 1),
    ([8,1], 6.0, 1),
    ([4,2,7,1,3,5,8], 3.72, 2),
    ([4,2,7,1,3,5,8], 3.14, 3),
    ([4,2,7,1,3,5,8], 5.14, 4),
    ([4,2,7,1,3,5,8], 5.98, 2),
    ([4,2,7,1,3,5,8], 6.18, 4),
    ([4,2,7,1,3,5,8], 7.12, 3),
    ([8,5,17,3,7,14,19,1,4,6,None,10,16,None,None,None,None,None,None,None,None,9,12,15,None,None,None,11,13], 6.18, 8),
  ]
  cases = [
    (listToTreeNode(x), target, k) for x, target, k in cases
  ]
  rslts = [
    solver.closestKValues(root, target, k) for root, target, k in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs[0].display()}, {cs[1:]} | solution: {rs}")     