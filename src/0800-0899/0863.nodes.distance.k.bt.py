from typing import List
from collections import defaultdict, deque
from config.treenode import TreeNode, listToTreeNode

class Solution:
  def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
    # transform the tree to a graph and bfs.
    graph = defaultdict(set)
    # # inorder traversal
    # node, stack = root, []
    # while node or stack:
    #   while node:
    #     stack.append(node)
    #     if node.left:
    #       graph[node].add(node.left)
    #       graph[node.left].add(node)
    #     node = node.left
    #   node = stack.pop()
    #   if node.right:
    #     graph[node].add(node.right)
    #     graph[node.right].add(node)
    #   node = node.right
    # preorder traversal
    stack = [root, ]
    while stack:
      node = stack.pop()
      if node.right:
        graph[node].add(node.right)
        graph[node.right].add(node)
        stack.append(node.right)
      if node.left:
        graph[node].add(node.left)
        graph[node.left].add(node)
        stack.append(node.left)
    # bfs on graph
    queue, seen, ans = deque([(target, 0)]), set([target]), []
    while queue:
      node, dist = queue.popleft()
      if dist == K:
        ans.append(node.val)
      elif dist < K:
        for nuxt in graph[node]:
          if nuxt not in seen:
            seen.add(nuxt)
            queue.append((nuxt, dist + 1))
    return ans

# if __name__ == '__main__':  
#   solver = Solution()
#   cases = [
#     ([3,5,1,6,2,0,8,None,None,7,4], 5, 2),
#   ]
#   # NOTE: targetVal is not target, need the treenode reference itself in parameter.
#   cases = [
#     (listToTreeNode(x), targetVal, K) for x, targetVal, K in cases
#   ]
#   rslts = [
#     solver.distanceK(root, targetVal, K) for root, targetVal, K in cases
#   ]
#   for cs, rs in zip(cases, rslts):
#     print(f"case:\n{cs[0].display() if cs[0] else None} + {cs[1:]} | solution: {rs}")
