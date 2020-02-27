class Solution:
  def verifyPreorder(self, preorder: List[int]) -> bool:
    """TC: O(N), SC: O(1). Two pointers on root node and its left child, 
      i = 0, j = 1, preorder[i] > preorder[j] and preorder[j + 1], i -> i + 1, j -> j + 2
    """
    i, j = 0, 1
    while j < len(preorder):
      if preorder[i] < preorder[j]:
        return False
      if j + 1 < len(preorder) and preorder[i] > preorder[j + 1]:
        return False
      i += 1
      j += 2
    return True
        