from typing import List
from collections import defaultdict

class Solution:
  def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    """brute force over level k
    """
    kh = defaultdict(list)
    for h, k in people:
      kh[k].append(h)
    q = []
    for k in sorted(kh.keys()):
      for h in sorted(kh[k], reverse=True):
        n, i = 0, 0
        while n < k and i < len(q):
          if q[i][0] >= h:
            n += 1
          i += 1
        # print(f"{q=}, {k=}, {h=}, {i=}")
        q.insert(i, (h, k))
    return q

class Solution:
  def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    """direct insertion over height h, from tallest to shortest
      1. shorter ones are invisible to taller ones
      2. all taller ones are taller than shorter ones,
        so when a new shorter height come in, its index will be its index in current queue
    """
    people.sort(key=lambda hk: (-hk[0], hk[1]))
    queue = []
    for h, k in people:
      queue.insert(k, (h, k))
    return queue

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [[1,0]],
    [[1,0],[2,0]],
    [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]],
    [[2,4],[3,4],[9,0],[0,6],[7,1],[6,0],[7,3],[2,5],[1,1],[8,0]]
  ]
  rslts = [solver.reconstructQueue(people) for people in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")