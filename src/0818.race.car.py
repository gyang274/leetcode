class Solution:
  def racecar(self, target: int) -> int:
    if target == 0:
      return 0
    # d: instruction -> (position, speed)
    d, seen = {}, set([])
    # bfs
    queue = [('', 0, 1)]
    for i, p, s in queue:
      iA = i + 'A'
      pA = p + s
      sA = s * 2
      if pA == target:
        return len(iA)
      if pA > -1 and ('A', pA, sA) not in seen:
        seen.add(('A', pA, sA))
        queue.append((iA, pA, sA))
      iR = i + 'R'
      pR = p
      sR = -1 if s > 0 else 1
      if pR > -1 and ('R', pR, sR) not in seen:
        seen.add(('R', pR, sR))
        queue.append((iR, pR, sR))
    return -1

import heapq

class Solution:
  def racecar(self, target: int) -> int:
    # dijkstra algorithm
    # K: bound s.t. 2 ^ K > target, so A^k is enough
    K = target.bit_length() + 1
    # b: bound or say barrier
    b = 1 << K
    # d: dist -> step
    d = [float('inf')] * (2 * b + 1)
    d[target] = 0
    # q: (step, dist)
    q = [(0, target)]
    while q:
      # s, t: step, dist
      s, t = heapq.heappop(q)
      if d[t] > s:
        continue
      # make a move of A^k R
      for k in range(K + 1):
        m = (1 << k) - 1
        # u, v: s-next, t-next
        u, v = s + k + 1, m - t
        if m == t:
          u -= 1
        if abs(v) <= b and u < d[v]:
          heapq.heappush(q, (u, v))
          d[v] = u
    return d[0]
        
class Solution:
  def racecar(self, target: int) -> int:
    # dynamic programming
    dp = [0, 1, 4] + [float('inf')] * target
    for t in range(3, target + 1):
      k = t.bit_length()
      if t == (1 << k) - 1:
        dp[t] = k
        continue
      for j in range(k - 1):
        dp[t] = min(dp[t], dp[t - (1 << (k - 1)) + (1 << j)] + k - 1 + j + 2)
      if (1 << k) - 1 - t < t:
        dp[t] = min(dp[t], dp[(1 << k) - 1 - t] + k + 1)
    return dp[target]

class Solution:
  def __init__(self):
    self.dp = {0: 0}
  def racecar(self, target: int) -> int:
    # dynamic programming
    t = target
    if t in self.dp:
      return self.dp[t]
    k = t.bit_length()
    if (1 << k) - 1 == t:
      self.dp[t] = k
    else:
      # option 1: A^k to 2^k-1, R, and then recursive call to go 2^k - 1 - t
      self.dp[t] = self.racecar((1 << k) - 1 - t) + k + 1
      for j in range(k - 1):
        # option 2: A^(k-1) to 2^(k-1)-1, R, back to t - (2^(k-1)-1) + 2^j-1 and then R, and A^j to t
        self.dp[t] = min(self.dp[t], self.racecar(t - (1 << (k - 1)) + (1 << j)) + k - 1 + j + 2)
    return self.dp[t]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2, 3, 5, 8,
  ]
  rslts = [solver.racecar(target) for target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
