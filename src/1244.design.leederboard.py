from collections import defaultdict

import heapq

class Leaderboard:

  def __init__(self):
    # u: user -> score
    self.u = defaultdict(lambda: 0)
    # q: (-score, user)
    self.q = []

  def addScore(self, playerId: int, score: int) -> None:
    self.u[playerId] -= score
    heapq.heappush(self.q, (self.u[playerId], playerId))
  
  def top(self, K: int) -> int:
    x = []
    while len(x) < K:
      s, i = heapq.heappop(self.q)
      if i in self.u and self.u[i] == s:
        x.append((s, i))
    for s, i in x:
      heapq.heappush(self.q, (s, i))
    return -sum([s for s, i in x])

  def reset(self, playerId: int) -> None:
    self.u.pop(playerId)