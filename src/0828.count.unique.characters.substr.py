class Solution:
  def uniqueLetterString(self, s: str) -> int:
    n, t = len(s), set(s)
    # X..<l-characters-from-seen-same>..X..<r-characters-until-seen-same>..X => counts: + (l + 1) * (r + 1)
    l, d = [-1] * n, {x: -1 for x in t}
    for i, x in enumerate(s):
      l[i], d[x] = d[x], i
    r, d = [n] * n, {x: n for x in t}
    for i, x in reversed(list(enumerate(s))):
      r[i], d[x] = d[x], i
    # counts
    counts = 0
    for i in range(n):
      counts += (i - l[i]) * (r[i] - i)
    return counts

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "LEETCODE",
  ]
  rslts = [solver.uniqueLetterString(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
