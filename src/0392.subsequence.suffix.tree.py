class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    # https://en.wikipedia.org/wiki/suffix_tree
    i, j, n, m = 0, 0, len(s), len(t)
    while i < n and j < m:
      if s[i] == t[j]:
        i += 1
        j += 1
      else:
        j += 1
    return i == n

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("abc", "ahbgdc"),
    ("axc", "ahbgdc"),
  ]
  rslts = [solver.isSubsequence(s, t) for s, t in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
