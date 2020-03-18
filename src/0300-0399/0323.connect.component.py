from typing import List
from collections import defaultdict, deque

class Solution:
  def countComponents(self, n: int, edges: List[List[int]]) -> int:
    # preprocessing edges into dict
    e = defaultdict(set)
    for x, y in edges:
      e[x].add(y)
      e[y].add(x)
    # n: number of connect componenet
    n, unvisited = 0, set([i for i in range(n)])
    while unvisited:
      n += 1
      q = deque([unvisited.pop(), ])
      while q:
        x = q.popleft()
        if x in e:
          for y in e.pop(x):
            e[y].remove(x)
            # if y in unvisited:
            #   q.append(y)
            # y must be unvisited since e[y].remove(x) in earlier step..
            q.append(y)
        unvisited.discard(x)
    return n

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (5, []),
    (5, [[0, 1], [2, 3]]),
    (5, [[0, 1], [1, 2], [3, 4]]),
    (5, [[0, 1], [1, 2], [2, 3], [3, 4]]),
  ]
  rslts = [solver.countComponents(n, edges) for n, edges in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")