from collections import deque

class Solution:
  def levelOrder(self, root: 'Node') -> List[List[int]]:
    x = []
    if root:
      queue, bound = deque([root,]), deque([])
      while queue:
        x.append([])
        while queue:
          node = queue.popleft()
          x[-1].append(str(node.val))
          for nc in node.children:
            bound.append(nc)
        queue, bound = bound, deque([])
    return x

# []
# [1]
# [1,null,3,2,4,null,5,6]
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]