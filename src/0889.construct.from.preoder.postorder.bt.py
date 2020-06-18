from typing import List
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, pre, post):
    node = TreeNode(pre[0])
    # i is the index on post matches pre[1]
    # pre[1] is the root of the left subtree
    i = len(post) - 2
    while i > -1 and not pre[1] == post[i]:
      i -= 1
    if i >= 0:
      node.left = self.recursive(pre[1:(i + 2)], post[:(i + 1)])
      if i < len(post) - 2:
        node.right = self.recursive(pre[(i + 2):], post[(i + 1):-1])
    return node
  def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
    # preorder: (root, left, right)
    # postorder: (left, right, root)
    # key: pre[0] == post[-1] for any given subtree
    return self.recursive(pre, post)

class Solution:
  def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
    if not pre:
      return None
    root = TreeNode(pre[0])
    if len(pre) == 1:
      return root
    i = post.index(pre[1]) + 1
    root.left = self.constructFromPrePost(pre[1:(i + 1)], post[:i])
    root.right = self.constructFromPrePost(pre[i + 1:], post[i:-1])
    return root

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,1], [1,2]),
    ([1,2,4,5,3,6,7], [4,5,2,6,7,3,1]),
  ]
  rslts = [solver.constructFromPrePost(pre, post) for pre, post in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution:\n{rs.display() if rs else None}")
