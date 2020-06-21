import heapq

class Solution:
  def orderlyQueue(self, S: str, K: int) -> str:
    q = []
    while True:
      s = ''
      for x in S:
        if len(q) == K:
          s += heapq.heappop(q)
        heapq.heappush(q, x)
      while q:
        s += heapq.heappop(q)
      s = min(s[i:] + s[:i] for i in range(len(s)))
      if s < S:
        S = s
      else:
        break
    return S

class Solution:
  def orderlyQueue(self, S: str, K: int) -> str:
    return min(S[i:] + S[:i] for i in range(len(S))) if K == 1 else "".join(sorted(S))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("leetcode", 1),
    ("leetcode", 2),
    ("leetcode", 3),
  ]
  rslts = [solver.orderlyQueue(S, K) for S, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
