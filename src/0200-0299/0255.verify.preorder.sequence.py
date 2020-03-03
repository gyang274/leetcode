from typing import List

class Solution:
  def verifyPreorder(self, preorder: List[int]) -> bool:
    """preorder: (root, left, right), bst: root > any_left, root < any_right
    """
    # imagine xroot hold the root value, and we always travel on its right subtree
    xroot, stack = float("-inf"), []
    for x in preorder:
      while stack and stack[-1] < x:
        xroot = stack.pop()
      if x > xroot:
        stack.append(x)
      else:
        return False
    return True

class Solution:
  def verifyPreorder(self, preorder: List[int]) -> bool:
    """preorder: (root, left, right), bst: root > any_left, root < any_right
    """
    # imagine xroot hold the root value (lower), and we always travel on its right subtree
    xroot, stack = -1 << 31, []
    for x in preorder:
      if x < xroot:
        return False
      while stack and x > stack[-1]:
        xroot = stack.pop()
      stack.append(x)
    return True

class Solution:
  def verifyPreorder(self, preorder: List[int]) -> bool:
    """preorder: (root, left, right), bst: root > any_left, root < any_right
      TC: O(N), SC: O(1), use a pointer on preorder, instead of hold a stack
      -> issue: input preorder is disrupted!
    """
    xroot, i = float("-inf"), 0
    for x in preorder:
      if x < xroot:
        return False
      while i > 0 and x > preorder[i - 1]:
        xroot = preorder[i - 1]
        i -= 1
      preorder[i] = x
      i += 1
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [1],
    [1,2],
    [2,1],
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    [3,2,1],
    [5,2,6,1,3],
    [5,2,1,3,6],
  ]
  rslts = [solver.verifyPreorder(preorder) for preorder in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")