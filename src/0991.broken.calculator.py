import heapq

class Solution:
  def brokenCalc(self, X: int, Y: int) -> int:
    if X >= Y:
      return X - Y
    queue, seen = [(0, X)], {X: 0}
    while queue:
      d, x = heapq.heappop(queue)
      if x == Y:
        return d
      if seen[x] >= d:
        seen[x] = d
        if x - 1 not in seen or seen[x - 1] > d + 1:
          seen[x - 1] = d + 1
          heapq.heappush(queue, (d + 1, x - 1))
        if x * 2 not in seen or seen[x * 2] > d + 1:
          seen[x * 2] = d + 1
          heapq.heappush(queue, (d + 1, x * 2))
    return -1

class Solution:
  def brokenCalc(self, X: int, Y: int) -> int:
    if X >= Y:
      return X - Y
    if Y & 1:
      return self.brokenCalc(X, Y + 1) + 1
    return self.brokenCalc(X, Y >> 1) + 1

class Solution:
  def brokenCalc(self, X: int, Y: int) -> int:
    count = 0
    while X < Y:
      if Y & 1:
        Y += 1
      else:
        Y >>= 1
      count += 1
    return count + X - Y

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, 3),
    (3, 5),
    (5, 8),
    (3, 10),
    (1, 1000000000),
  ]
  rslts = [solver.brokenCalc(X, Y) for X, Y in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
