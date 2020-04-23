from typing import List
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def printTree(self, root: TreeNode) -> List[List[str]]:
    ans, queue, depth = [], [root], 0
    # set ans with values
    while any(queue):
      depth += 1
      ans.append([str(node.val) if node else "" for node in queue])
      qnext = []
      for node in queue:
        if node:
          qnext.append(node.left if node.left else "")
          qnext.append(node.right if node.right else "")
        else:
          qnext.append("")
          qnext.append("")
      queue = qnext
    # set ans with sparator ""s
    for level in range(1, depth + 1):
      # n: num of node on level
      n = 1 << (level - 1)
      # s: num of separator "" at level
      s = (1 << (depth - level)) - 1
      ans[level - 1][n:n] = [""] * s
      for i in range(n - 1, 0, -1):
        ans[level - 1][i:i] = [""] * (2 * s + 1)
      ans[level - 1][0:0] = [""] * s
    return ans

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,None,2,3],
  ]
  cases = [
    (listToTreeNode(x)) for x in cases
  ]
  rslts = [
    solver.printTree(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None}, solution: {rs}")
