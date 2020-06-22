from typing import List

class Solution:
  def dfs(self, path, node):
    if node in self.terminal:
      return False
    if node in path or node in self.cycle:
      self.cycle.add(node)
      return True
    path.add(node)
    for nuxt in self.graph[node]:
      if self.dfs(path, nuxt):
        self.cycle.add(node)
        return True
    self.terminal.add(node)
    return False
  def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
    self.cycle, self.terminal = set([]), set([])
    for node, edges in enumerate(graph):
      if not edges:
        self.terminal.add(node)
    self.graph = graph
    for node in range(len(graph)):
      if node not in self.cycle and node not in self.terminal:
        self.dfs(set([]), node)
    return sorted(self.terminal)

class Solution:
  def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
    # nodes connects to ONLY terminal nodes are safe..
    n = len(graph)
    safe = [False] * n
    graph = list(map(set, graph))
    rgraph = [set() for i in range(n)]
    queue = []
    for i, js in enumerate(graph):
      if not js:
        queue.append(i)
      for j in js:
        rgraph[j].add(i)
    while queue:
      j = queue.pop()
      safe[j] = True
      for i in rgraph[j]:
        graph[i].remove(j)
        if len(graph[i]) == 0:
          queue.append(i)
    return [i for i, v in enumerate(safe) if v]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,2],[2,3],[5],[0],[5],[],[]],
  ]
  rslts = [solver.eventualSafeNodes(graph) for graph in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
