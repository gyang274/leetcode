from typing import List
from config.treenode import TreeNode, listToTreeNode
from collections import deque

class Solution:
  def verticalOrder(self, root: TreeNode) -> List[List[int]]:
    if not root: return []
    # ridx: root vertical level in ans
    ridx, stack, ans = 0, deque([(root, 0), ]), deque([])
    while stack:
      node, idx = stack.popleft()
      while ridx + idx < 0:
        ans.appendleft([])
        ridx += 1
      while ridx + idx >= len(ans):
        ans.append([])
      ans[ridx + idx].append(node.val)
      if node.left:
        stack.append((node.left, idx - 1))
      if node.right:
        stack.append((node.right, idx + 1))
    return ans

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [],
    [1,None,2,3],
    [3,9,20,None,None,15,7],
    [3,9,8,4,0,1,7],
    [3,9,8,4,0,1,7,None,None,None,2,5]
  ]
  cases = [
    (listToTreeNode(x)) for x in cases
  ]
  rslts = [
    solver.verticalOrder(x) for x in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case:\n{cs.display() if cs else None} | solution: {rs}")