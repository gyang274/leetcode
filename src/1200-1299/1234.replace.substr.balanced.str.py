from collections import Counter

class Solution:
  def balancedString(self, s: str) -> int:
    # O(N), two pointer
    i, j, h, n = 0, 0, Counter(s), len(s)
    for x in 'QWER':
      h[x] -= n // 4
    if all(h[x] == 0 for x in 'QWER'):
      return 0
    m, k = n, {x: 0 for x in 'QWER'}
    while j < n:
      while j < n and any(k[x] < h[x] for x in 'QWER'):
        k[s[j]] += 1
        j += 1
      m = min(m, j - i)
      while i < n and all(k[x] >= h[x] for x in 'QWER'):
        k[s[i]] -= 1
        i += 1
      m = min(m, j - i + 1)
    return m

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "QWER",
    "QQQQ",
    "QQWWWWRR",
    "QQQQRRRR",
    "QWQRQWQR",
  ]
  rslts = [solver.balancedString(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
