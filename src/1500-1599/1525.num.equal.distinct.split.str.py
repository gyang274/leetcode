class Solution:
  def numSplits(self, s: str) -> int:
    n = len(s)
    l, u = [0] * n, set()
    for i in range(n):
      l[i] = l[i - 1]
      if s[i] not in u:
        l[i] += 1
        u.add(s[i])
    r, v = [0] * n, set()
    for i in range(1, n + 1):
      r[-i] = r[-i + 1]
      if s[-i] not in v:
        r[-i] += 1
        v.add(s[-i])
    count = 0
    for i in range(n - 1):
      if l[i] == r[i + 1]:
        count += 1
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "aacaba",
    "acbadbaada",
  ]
  rslts = [solver.numSplits(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
