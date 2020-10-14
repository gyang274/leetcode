import heapq

class Solution:
  def longestDiverseString(self, a: int, b: int, c: int) -> str:
    q = []
    if a > 0:
      heapq.heappush(q, [-a, 'a'])
    if b > 0:
      heapq.heappush(q, [-b, 'b'])
    if c > 0:
      heapq.heappush(q, [-c, 'c'])
    s = ''
    while q:
      # x: extender
      x = heapq.heappop(q)
      if s and s[-1] == x[1]:
        s += x[1] * min(-x[0], 1)
        x[0] += 1
      else:
        s += x[1] * min(-x[0], 2)
        x[0] += 2
      # y: separator
      if q:
        y = heapq.heappop(q)
        s += y[1] * min(-y[0], 1)
        y[0] += 1
        if y[0] < 0:
          heapq.heappush(q, y)
        if x[0] < 0:
          heapq.heappush(q, x)
    return s

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (1, 1, 7),
    (2, 2, 3),
    (7, 1, 0),
    (8, 9, 72),
    (23, 42, 85),
    (4, 4, 3),
  ]
  rslts = [solver.longestDiverseString(a, b, c) for a, b, c in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
