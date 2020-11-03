from typing import List
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def getLonelyNodes(self, root: TreeNode) -> List[int]:
    queue, ans = [root], []
    for node in queue:
      if node.left and node.right:
        queue.append(node.left)
        queue.append(node.right)
      elif node.left:
        queue.append(node.left)
        ans.append(node.left.val)
      elif node.right:
        queue.append(node.right)
        ans.append(node.right.val)
    return ans

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,None,2,3],
    [1,2,3,None,4],
    [7,1,4,6,None,5,3,None,None,None,None,None,2],
  ]
  cases = [
    listToTreeNode(x) for x in cases
  ]
  rslts = [
    solver.getLonelyNodes(root) for root in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")
