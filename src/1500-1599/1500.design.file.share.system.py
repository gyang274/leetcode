from collections import defaultdict

import heapq

class FileSharing:

  def __init__(self, m: int):
    self.chunkOwner = defaultdict(set)
    self.userIDs = []
    self.userChunks = {}
    self.i = 1

  def join(self, ownedChunks: List[int]) -> int:
    if self.userIDs:
      u = heapq.heappop(self.userIDs)
    else:
      u = self.i
      self.i += 1
    self.userChunks[u] = set(ownedChunks)
    for x in self.userChunks[u]:
      self.chunkOwner[x].add(u)
    return u

  def leave(self, userID: int) -> None:
    for x in self.userChunks[userID]:
      self.chunkOwner[x].remove(userID)
    self.userChunks.pop(userID)
    if userID + 1 == self.i:
      self.i -= 1
    else:
      heapq.heappush(self.userIDs, userID)

  def request(self, userID: int, chunkID: int) -> List[int]:
    users = sorted(self.chunkOwner[chunkID])
    if users:
      self.chunkOwner[chunkID].add(userID)
      self.userChunks[userID].add(chunkID)
    return users