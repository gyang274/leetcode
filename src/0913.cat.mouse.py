from typing import List
from collections import defaultdict, deque

class Solution:
  def catMouseGame(self, graph: List[List[int]]) -> int:
    # instead of working on the original graph, work on the augmented graph of (mouse-node, cat-node, mouse-or-cat-turn)
    # let (1, 2, 1) be mouse on node 1, cat on node 2 and mouse's turn to move, this is the init of the game,
    # let (0, _, 1/2) be ende of game with mouse win, and (i, i, 2/1) be ende of game with cat win, derive backward.
    n = len(graph)
    # create the nodes of augmented graph (m, c, t) with win status, t = 1 mouse's turn, 2 cat's turn.
    nodes = {}
    for i in range(n):
      for j in range(1, n):
        for k in range(1, 3):
          # unknown yet, default to draw
          nodes[(i, j, k)] = 0
          if i == 0:
            # mouse win
            nodes[(i, j, k)] = 1
          elif i == j:
            # cat win
            nodes[(i, j, k)] = 2
    # create the edges of augmented graph, bipartite graph, as mouse-turn <-> cat-turn
    # reversed connections for backward derivation
    # edges[(i, j, k)]: nodes can move to (i, j, k), NOT nodes can be moved from (i, j, k)
    edges = defaultdict(set)
    for i in range(n):
      for j in range(1, n):
        for iprev in graph[i]:
          edges[(i, j, 2)].add((iprev, j, 1))
        for jprev in graph[j]:
          if jprev > 0:
            edges[(i, j, 1)].add((i, jprev, 2))
    # track the degree to determine any unseen move, e.g., from which node to this node, if not then draw.
    degree = {}
    for i in range(n):
      for j in range(1, n):
        degree[(i, j, 1)] = len(graph[i])
        degree[(i, j, 2)] = len(graph[j]) - (0 in graph[j])
    # minimax game strategy, derive backward
    queue = deque([])
    for i in range(n):
      # mouse wins
      queue.append((0, i, 1, 1))
      queue.append((0, i, 2, 1))
      if i > 0:
        # cat wins
        queue.append((i, i, 1, 2))
        queue.append((i, i, 2, 2))
    # percolate
    while queue:
      i, j, k, s = queue.popleft()
      # all nodes (iprev, jprev, kprev) s.t. can move to (i, j, k)
      for iprev, jprev, kprev in edges[(i, j, k)]:
        # undetermined
        if nodes[(iprev, jprev, kprev)] == 0:
          # move and make me win
          if kprev == s:
            # make the move, mark this is possible to win by making this move
            nodes[(iprev, jprev, kprev)] = s
            queue.append((iprev, jprev, kprev, s))
          else:
            # mark down degree to 
            degree[(iprev, jprev, kprev)] -= 1
            # degree == 0 means all subsequential moves of (iprev, jprev, kprev) leads to the opponent win..
            if degree[(iprev, jprev, kprev)] == 0:
              # admit the loss
              nodes[(iprev, jprev, kprev)] = 3 - kprev
              queue.append((iprev, jprev, kprev, 3 - kprev))
    return nodes[(1, 2, 1)]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,3],[0],[3],[0,2]],
    [[2,3],[3,4],[0,4],[0,1],[1,2]],
    [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]],
  ]
  rslts = [solver.catMouseGame(graph) for graph in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
