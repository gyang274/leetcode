from typing import List
from collections import defaultdict

class Node:
  def __init__(self, val):
    self.val = val
    self.dist = 0
    self.count = 0
    self.parent = None
    self.children = []
    self.distance = []

class Solution:
  def dfs1(self, node):
    node.distance = [self.dfs1(nc) for nc in node.children]
    if node.distance:
      x, y = zip(*node.distance)
      node.dist += sum(x)
      node.count += sum(y)
    return node.dist + node.count + 1, node.count + 1
  def dfs2(self, node, ncdist, nccount):
    if node.parent:
      node.dist += node.parent.dist - ncdist + node.parent.count - nccount + 1
      node.count += node.parent.count - nccount + 1
    for nc, (ncdist, nccount) in zip(node.children, node.distance):
      self.dfs2(nc, ncdist, nccount)
  def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
    nodes = [Node(i) for i in range(N)]
    d = defaultdict(set)
    for i, j in edges:
      d[i].add(j)
      d[j].add(i)
    # construct the tree
    queue, seen = [0], set([0])
    while queue:
      i = queue.pop()
      js = d[i] - seen
      seen.update(js)
      queue.extend(js)
      nodes[i].children = [nodes[j] for j in js]
      for j in js:
        nodes[j].parent = nodes[i]
    # dfs over tree to get children's dist
    self.dfs1(nodes[0])
    # dfs over tree to get parent's and siblings' dist
    self.dfs2(nodes[0], 0, 0)
    return [nodes[i].dist for i in range(N)]

class Solution:
  def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
    graph = defaultdict(set)
    for u, v in edges:
      graph[u].add(v)
      graph[v].add(u)
    # dfs1 + dfs2 use dict
    count = [1] * N
    ans = [0] * N
    def dfs1(node = 0, parent = None):
      for child in graph[node]:
        if child != parent:
          dfs1(child, node)
          count[node] += count[child]
          ans[node] += ans[child] + count[child]
    def dfs2(node = 0, parent = None):
      for child in graph[node]:
        if child != parent:
          ans[child] = ans[node] - count[child] + N - count[child]
          dfs2(child, node)
    dfs1(0, None)
    dfs2(0, None)
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [6, [[0,1],[0,2],[2,3],[2,4],[2,5]]],
  ]
  rslts = [solver.sumOfDistancesInTree(N, edges) for N, edges in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
