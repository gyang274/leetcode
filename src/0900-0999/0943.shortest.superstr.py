from typing import List

import heapq

class Solution:
  def shortestSuperstring(self, A: List[str]) -> str:
    """directed graph shortest Hamilton path
      node(i) = A[i], edge(i, j) = -overlap(A[i], A[j]) or len(A[i]) + len(A[j]) - 2 * overlap(A[i], A[j])
    """
    n, L = len(A), list(map(len, A))
    # construct the graph
    W = [[0] * n for _ in range(n)]
    for i, x in enumerate(A):
      for j, y in enumerate(A):
        if i != j:
          for k in range(min(L[i], L[j]), -1, -1):
            if x.endswith(y[:k]):
              W[i][j] = k
              break
    M = (1 << n) - 1
    # s (source node S) -> <complete graph of all nodes> -> t (target node T or -1)
    # directed graph shortest Hamilton path => shortest path visit each node from s -> .. -> t
    # queue: dist, node, mask, seqn
    # queue init path with s -> ..
    q = [(L[i], i, (1 << i), [i]) for i in range(n)]
    heapq.heapify(q)
    while q:
      dist, i, mask, seqn = heapq.heappop(q)
      if mask == -1:
        ans = A[seqn[0]]
        for j in range(1, n):
          ans += A[seqn[j]][W[seqn[j - 1]][seqn[j]]:]
        return ans
      if mask == M:
        # queue ende path with .. -> t
        heapq.heappush(q, (dist + L[i], -1, -1, seqn))
      for j in range(n):
        if ((mask >> j) & 1) ^ 1:
          heapq.heappush(q, (dist + L[i] + L[j] - 2 * W[i][j], j, mask | (1 << j), seqn + [j]))

class Solution:
  def shortestSuperstring(self, A: List[str]) -> str:
    # dynamic programming
    # dp(mask ^ (1<<j), j) = max(overlap(A[i], A[j]) + dp(mask, i))
    # where dp(mask, i) is the min length of putting words in mask ende with A[i]
    n = len(A)
    # populate overlaps
    overlaps = [[0] * n for _ in range(n)]
    for i, x in enumerate(A):
      for j, y in enumerate(A):
        if i != j:
          for k in range(min(len(x), len(y)), -1, -1):
            if x.endswith(y[:k]):
              overlaps[i][j] = k
              break
    # dp[mask][i] = most overlap with mask, ending with ith element
    dp = [[0] * n for _ in range(1 << n)]
    parent = [[None] * n for _ in range(1 << n)]
    for mask in range(1, 1 << n):
      for bit in range(n):
        if (mask >> bit) & 1:
          # Let's try to find dp[mask][bit].
          # Previously, we had a collection of items represented by pmask.
          pmask = mask ^ (1 << bit)
          if pmask == 0:
            continue
          for i in range(n):
            if (pmask >> i) & 1:
              # For each bit i in pmask, calculate the value
              # if we ended with word i, then added word 'bit'.
              value = dp[pmask][i] + overlaps[i][bit]
              if value > dp[mask][bit]:
                dp[mask][bit] = value
                parent[mask][bit] = i
    # Answer will have length sum(len(A[i]) for i) - max(dp[-1])
    # Reconstruct answer:
    # Follow parents down backwards path that retains maximum overlap
    perm = []
    mask = (1 << n) - 1
    i = max(range(n), key = dp[-1].__getitem__)
    while i is not None:
      perm.append(i)
      mask, i = mask ^ (1 << i), parent[mask][i]
    # Reverse path to get forwards direction; add all remaining words
    perm = perm[::-1]
    seen = [False] * n
    for x in perm:
      seen[x] = True
    perm.extend([i for i in range(n) if not seen[i]])
    # Reconstruct answer given perm = word indices in left to right order
    ans = A[perm[0]]
    for i in range(1, len(perm)):
        ans += A[perm[i]][overlaps[perm[i - 1]][perm[i]]:]
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["alex","lexle","leetcode"],
    ["catg","ctaagt","gcta","ttca","atgcatc"],
    ["ppgortnmsy","czmysoeeyugbiylso","nbfzpppvhbjydtx","rnzynedhoiunkpon","ornzynedhoiunkpo","ylsomoktkyfgljcf","jtvkrornzynedhoiunk","hvhhihwdffmxnczmyso","ktkyfgljcfbkqcpp","nzynedhoiunkponbfz","nedhoiunkponbfzpppvh"],
  ]
  rslts = [solver.shortestSuperstring(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
