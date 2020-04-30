from typing import List
from config.treenode import TreeNode, listToTreeNode
from collections import defaultdict, Counter

class Solution:
  def lookup(self, node):
    if not node:
      return -1
    uid = self.trees[node.val, self.lookup(node.left), self.lookup(node.right)]
    self.count[uid] += 1
    if self.count[uid] == 2:
      self.ans.append(node)
    return uid
  def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
    # hashmap: (root, left-subtree, right-subtree) to unique identifier
    self.trees = defaultdict()
    self.trees.default_factory = self.trees.__len__
    self.count = Counter()
    self.ans = []
    self.lookup(root)
    return self.ans

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,None,2,3],
    [1,2,3,4,None,2,4,None,None,4],
    [1,2,3,4,None,2,4,None,None,4,2],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.findDuplicateSubtrees(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
