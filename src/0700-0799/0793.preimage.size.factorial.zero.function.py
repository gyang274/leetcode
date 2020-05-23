class Solution:
  def zeta(self, n):
    count = 0
    while n:
      count += n // 5
      n //=5
    return count
  def preimageSizeFZF(self, K: int) -> int:
    """O(logK * logK), binary search + zeta.
    """
    l, r = 4 * K, 5 * K + 10
    while l < r:
      m = l + (r - l) // 2
      k = self.zeta(m)
      if k == K:
        return 5
      elif k > K:
        r = m
      else:
        l = m + 1
    return 0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    0, 1, 2, 3, 5, 8, 23, 42,
  ]
  rslts = [solver.preimageSizeFZF(K) for K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
