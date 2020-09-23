from typing import List
from collections import defaultdict, Counter
from itertools import chain

class Solution:
  def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
    # bfs + sort
    graph = defaultdict(set)
    for u, vs in enumerate(friends):
      for v in vs:
        graph[u].add(v)
        graph[v].add(u)
    # bfs: nodes at i-th level 
    queue, qlvl, seen = set([id]), 0, set([id])
    while queue and qlvl < level:
      qnext = set()
      for u in queue:
        for v in graph[u]:
          if v not in seen:
            qnext.add(v)
            seen.add(v)
      queue = qnext
      qlvl += 1
    # sort: watched videos by frequency
    videos = Counter(list(chain.from_iterable([watchedVideos[u] for u in queue])))
    return [v for c, v in sorted((videos[v], v) for v in videos)]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([["A","B"],["C"],["B","C"],["D"]], [[1,2],[0,3],[0,3],[1,2]], 0, 1),
    ([["A","B"],["C"],["B","C"],["D"]], [[1,2],[0,3],[0,3],[1,2]], 1, 1),
    ([["A","B"],["C"],["B","C"],["D"]], [[1,2],[0,3],[0,3],[1,2]], 0, 2),
    ([["A","B"],["C"],["B","C"],["D"]], [[1,2],[0,3],[0,3],[1,2]], 2, 2),
    ([["A","B"],["C"],["B","C"],["D"]], [[1,2],[0,3],[0,3],[1,2]], 2, 3),
  ]
  rslts = [solver.watchedVideosByFriends(watchedVideos, friends, id, level) for watchedVideos, friends, id, level in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
