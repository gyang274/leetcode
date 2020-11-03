import bisect

class Solution:
  def counter(self, s, i, m, n):
    # count num of arrays with sum <= s
    if i == m - 1:
      return bisect.bisect(self.mat[m - 1], s)
    else:
      count = 0
      for j in range(n):
        snext = s - self.mat[i][j]
        if snext > 0:
          count += self.counter(snext, i + 1, m, n)
      return count
  def kthSmallest(self, mat, k):
    m, n = len(mat), len(mat[0])
    self.mat = mat
    l, r = sum([mat[i][0] for i in range(m)]), sum([mat[i][-1] for i in range(m)]) + 1
    while l < r:
      s = l + (r - l) // 2
      if self.counter(s, 0, m, n) >= k:
        r = s
      else:
        l = s + 1
    return l

import heapq

class Solution:
  def kthSmallest(self, mat, k):
    m, n = len(mat), len(mat[0])
    seen = set([tuple([0] * m)])
    queue = [(sum([mat[i][0] for i in range(m)]), [0] * m)]
    # if k == 1:
    #   return queue[0][0]
    for _ in range(k):
      z, js = heapq.heappop(queue)
      for i, j in enumerate(js):
        if j + 1 < n:
          jsnext = js[:]
          jsnext[i] += 1
          jsnuxt = tuple(jsnext)
          if jsnuxt not in seen:
            seen.add(jsnuxt)
            heapq.heappush(queue, (z - mat[i][j] + mat[i][j + 1], jsnext))
    return z

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[1,3,11],[2,4,6]], 5),
    ([[1,3,11],[2,4,6]], 8),
    ([[1,10,10],[1,4,5],[2,3,6]], 7),
  ]
  rslts = [solver.kthSmallest(mat, k) for mat, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
