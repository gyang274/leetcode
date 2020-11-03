from typing import List

class DSU:
  def __init__(self, k):
    # representer
    self.reps = {}
    self.size = {}
    self.k = k
    self.m = 0
  def add(self, x):
    self.reps[x] = x
    self.size[x] = 1
  def find(self, x):
    while not x == self.reps[x]:
      x = self.reps[x]
    return x
  def union(self, x, y):
    hX = self.find(x)
    hY = self.find(y)
    if not hX == hY:
      h = min(hX, hY)
      if h == hX:
        self.reps[hY] = h
        self.m += (self.size[hX] + self.size[hY]) // self.k - self.size[hX] // self.k - self.size[hY] // self.k
        self.size[hX] += self.size[hY]
        self.size.pop(hY)
      else:
        self.reps[hX] = h
        self.m += (self.size[hX] + self.size[hY]) // self.k - self.size[hX] // self.k - self.size[hY] // self.k
        self.size[hY] += self.size[hX]
        self.size.pop(hX)

class Solution:
  def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
    n = len(bloomDay)
    if m * k > n:
      return -1
    if k == 1:
      return sorted(bloomDay)[m - 1]
    # dsu
    dsu = DSU(k)
    # day
    d, q, seen = -1, sorted([(x, i) for i, x in enumerate(bloomDay)], reverse=True), set()
    while q and dsu.m < m:
      d, i = q.pop()
      dsu.add(i)
      seen.add(i)
      if i - 1 in seen:
        dsu.union(i - 1, i)
      if i + 1 in seen:
        dsu.union(i, i + 1)
    return d # if dsu.m == m else -1

class Solution:
  def check(self, bloomDay, m, k, day):
    count, consecutive = 0, 0
    for d in bloomDay:
      if d <= day:
        consecutive += 1
        if consecutive >= k:
          count += 1
          if count >= m:
            return True
          consecutive = 0
      else:
        consecutive = 0
    return False
  def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
    # TC: O(NlogN), binary search
    l, r = min(bloomDay), max(bloomDay)
    while l < r:
      mid = (l + r) // 2
      if self.check(bloomDay, m, k, mid):
        r = mid
      else:
        l = mid + 1
    return l if self.check(bloomDay, m, k, l) else -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,4,3,5,2], 3, 1),
    ([1,4,3,5,2], 3, 2),
    ([1,1,1,1,7,1,1], 2, 3),
    ([1,10,2,9,3,8,4,7,5,6], 4, 2),
  ]
  rslts = [solver.minDays(bloomDay, m, k) for bloomDay, m, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
