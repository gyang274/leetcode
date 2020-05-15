from typing import List

import heapq, itertools

class Solution:
  def slidingPuzzle(self, board: List[List[int]]) -> int:
    """O(RC(RC)!): BFS or A* search. A* search: generalized Dijkstra algorithm.
    """
    m, n = len(board), len(board[0])
    init = tuple(itertools.chain(*board))
    ende = tuple(list(range(1, m * n)) + [0])
    # deadende.. parity of inversions.. half/half ende vs deadende.
    dead = tuple(list(range(1, m * n - 2)) + [m * n - 1, m * n - 2, 0])
    queue = [(0, 0, init, init.index(0))]
    costs = {init: 0}
    # hashmap: i-tile -> (r, c)
    expected = {(r * m + c + 1) % (m * n) : (r, c) for r in range(m) for c in range(n)}
    # heuristic esimate of distance from curr -> ende using manhattan distance
    def heuristic(board):
      d = 0
      for r in range(m):
        for c in range(n):
          v = board[m * r + c]
          if v == 0:
            continue
          er, ec = expected[v]
          d += abs(r - er) + abs(c - ec)
      return d
    while queue:
      # f: estimated distance (priority)
      # g: actual distance travelled (depth)
      f, g, curr, zero = heapq.heappop(queue)
      if curr == ende:
        return g
      if curr == dead:
        return -1
      if f > costs[curr]:
        continue
      for d in (-1, 1, -n, n):
        znxt = zero + d
        if not abs(zero // n - znxt // n) + abs(zero % n - znxt % n) == 1:
          continue
        if 0 <= znxt < m * n:
          nuxt = list(curr)
          nuxt[zero], nuxt[znxt] = nuxt[znxt], nuxt[zero]
          nuxt = tuple(nuxt)
          cnxt = g + 1 + heuristic(nuxt)
          if cnxt < costs.get(nuxt, float('inf')):
            costs[nuxt] = cnxt
            heapq.heappush(queue, (cnxt, g + 1, nuxt, znxt))
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,2,3],[4,0,5]],
    [[1,2,3],[5,4,0]],
    [[4,1,2],[5,0,3]],
    [[3,2,4],[1,5,0]],
  ]
  rslts = [solver.slidingPuzzle(board) for board in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
