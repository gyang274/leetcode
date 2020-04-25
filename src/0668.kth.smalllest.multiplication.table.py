class Solution:
  def findKthNumber(self, m: int, n: int, k: int) -> int:
    """O(min(m,n)log(m*n)), binary search + math.
    """
    m, n = min(m, n), max(m, n)
    l, r = 1, m * n
    while l < r:
      q = l + (r - l) // 2
      # count num of value p in multiplication table m x n, s.t. p <= q
      # on i-th row, i, 2 * i, .., n * i, p = o * i <= q -> o <= q // i
      count = sum([min(q // i, n) for i in range(1, m + 1)])
      if count >= k:
        r = q
      else:
        l = q + 1
    return l

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (3, 3, 5),
    (23, 42, 274),
  ]
  rslts = [solver.findKthNumber(m, n, k) for m, n, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
