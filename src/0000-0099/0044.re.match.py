class Solution:
  def isMatch(self, s: str, p: str) -> bool:
    """Dynatmic Programming.
    """
    # print(f"{s=}, {p=}")
    memo = {}
    def dp(i, j):
      if (i, j) not in memo:
        if j == len(p):
          ans = i == len(s)
        else:
          if i <= len(s) and p[j] == '*':
            ans = dp(i, j + 1) or dp(i + 1, j)
          else:
            f = i < len(s) and p[j] in {s[i], '?'}
            ans = f and dp(i + 1, j + 1)
        memo[(i, j)] = ans
        # print(f"{i=}, {j=}, {memo=}")
      return memo[(i, j)]
    return dp(0, 0)


class Solution:
  def isMatch(self, s: str, p: str) -> bool:
    """Backtracking: https://arxiv.org/pdf/1407.0950.pdf.
    """
    sl, pl = len(s), len(p)
    si, pi = 0, 0
    # wildcard * index, and index hold for backtracking
    wi = hi = -1 
    while si < sl:
      if pi < pl and p[pi] in {s[si], '?'}:
        si += 1
        pi += 1
      elif pi < pl and p[pi] == '*':
        wi = pi
        hi = si
        pi += 1
      elif wi == -1:
        return False
      else:
        pi = wi + 1
        si = hi + 1
        hi = si
    return all(x == '*' for x in p[pi:])


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ("", ""),
    ("a", ""),
    ("", "a"),
    ("a", "a"),
    ("a", "?"),
    ("a", "*"),
    ("a", "a*"),
    ("aa", "a"),
    ("aa", "?"),
    ("aa", "*"),
    ("aa", "a?"),
    ("aa", "a*"),
    ("aa", "a?*"),
    ("adceb", "*a*b"),
    ("acdcb", "a*c?b"),
  ]
  rslts = [solver.isMatch(s, p) for s, p in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  