class Solution:
  def getHappyString(self, n: int, k: int) -> str:
    s = ['a', 'b', 'c']
    for _ in range(n - 1):
      m = []
      for x in s:
        for y in ['a', 'b', 'c']:
          if not x[-1] == y:
            m.append(x + y)
      s = m
    s.sort()
    return s[k - 1] if len(s) >= k else ''

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (1, 3),
    (1, 4),
    (2, 7),
    (10, 100),
  ]
  rslts = [solver.getHappyString(n, k) for n, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
