from typing import List
from config.treenode import TreeNode, listToTreeNode


class Solution:
  def recursive(self, l, r) -> TreeNode:
    m = (l + r) // 2
    root = TreeNode(self.nums[m])
    if m > l:
      root.left = self.recursive(l, m)
    if m < r - 1:
      root.right = self.recursive(m + 1, r)
    return root
  def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    if not nums:
      return None
    self.nums = nums
    return self.recursive(0, len(nums))
    

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    # [],
    [1],
    [1, 2],
    [1, 2, 3],
    [1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 6, 7, 8],
  ]
  rslts = [
    solver.sortedArrayToBST(nums) for nums in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs}, solution:\n{rs.display()}")