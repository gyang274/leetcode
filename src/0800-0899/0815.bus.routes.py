from typing import List
from collections import defaultdict

class Solution:
  def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
    if S == T:
      return 0
    n, routes = len(routes), list(map(set, routes))
    # graph: bus route as node, none-empty intersection as edge
    # shortest path between any node (bus route contains S) in source to any node in target
    graph = defaultdict(set)
    for i in range(n):
      for j in range(i):
        if routes[i] & routes[j]:
          graph[i].add(j)
          graph[j].add(i)
    # source and target
    s = set(i for i, r in enumerate(routes) if S in r)
    t = set(i for i, r in enumerate(routes) if T in r)
    # bfs
    seen, queue, dist = s, s, 1
    while queue:
      if t & queue:
        return dist
      qnext = set()
      for r in queue:
        qnext |= graph[r] - seen
      queue = qnext
      dist += 1
      seen |= queue
    return -1

class Solution:
  def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
    if S == T:
      return 0
    n, routes = len(routes), list(map(set, routes))
    # graph: bus route as node, none-empty intersection as edge
    # shortest path between any node (bus route contains S) in source to any node in target
    graph = defaultdict(set)
    for i in range(n):
      for j in range(i):
        if routes[i] & routes[j]:
          graph[i].add(j)
          graph[j].add(i)
    # source and target
    s, t = set(), set()
    for node, route in enumerate(routes):
      if S in route:
        s.add(node)
      if T in route:
        t.add(node)
    # bfs
    queue = [(node, 1) for node in s]
    for node, dist in queue:
      if node in t:
        return dist
      for nuxt in graph[node] - s:
        queue.append((nuxt, dist + 1))
      s |= graph[node]
    return -1

class Solution:
  def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
    if S == T:
      return 0
    n, routes = len(routes), list(map(set, routes))
    # bfs over bus stops instead of routes
    # start with S explore reachable bus stops by taking all possible route, until reach T
    s2r = defaultdict(set)
    for i, route in enumerate(routes):
      for s in route:
        s2r[s].add(i)
    # start
    seen = set()
    for r in s2r[S]:
      seen |= routes[r]
    # bfs over bus stops
    queue = [(s, 1) for s in seen]
    for stop, dist in queue:
      if stop == T:
        return dist
      for r in s2r[stop]:
        for snxt in routes[r] - seen:
          queue.append((snxt, dist + 1))
      seen |= routes[r]
    return -1


if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[1,2,7], [3,6,7]], 1, 6),
  ]
  rslts = [solver.numBusesToDestination(routes, S, T) for routes, S, T in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
