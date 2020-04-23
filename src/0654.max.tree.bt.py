from typing import List
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, i, j):
    if i == j:
      return None
    imax = self.nums.index(max(self.nums[i:j]))
    root = TreeNode(self.nums[imax])
    root.left = self.recursive(i, imax)
    root.right = self.recursive(imax + 1, j)
    return root
  def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
    self.nums = nums
    self.n = n = len(nums)
    return self.recursive(0, n)

class Solution:
  def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
    if not nums:
      return None
    imax = nums.index(max(nums))
    root = TreeNode(nums[imax])
    root.left = self.constructMaximumBinaryTree(nums[:imax])
    root.right = self.constructMaximumBinaryTree(nums[(imax + 1):])
    return root

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [3,2,1,6,0,5,4],
  ]
  rslts = [
    solver.constructMaximumBinaryTree(nums) for nums in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs}, solution:\n{rs.display() if rs else None}")
