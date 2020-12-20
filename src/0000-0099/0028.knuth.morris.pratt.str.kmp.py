class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    """Simple O(nm) solution."""
    n = len(needle)
    for i in range(0, len(haystack) - n  + 1):
      if haystack[i:(i + n)] == needle:
        return i
    return -1

class Solution:
  def strStr(self, s: str, p: str) -> int:
    """Knuth-Morris-Pratt (KMP) Algorithm.
    """
    n, m = len(s), len(p)
    # corner case
    if m == 0: return 0
    # construct the \pi reference table
    u = [-1 for _ in range(m + 1)]
    k = -1
    for i in range(1, m + 1):
      while k >= 0 and p[k] != p[i - 1]:
        k = u[k]
      k += 1
      u[i] = k
    # print(u)
    # match with push forward w.r.t \pi
    i = 0
    j = 0
    k = 0
    while i < n:
      j = max(0, k)
      # print('outer', i, j, k)
      while i + j < n and j < m and s[i + j] == p[j]:
        j += 1
        # print('inner', i, j, k)
        if j == m:
          return i
      k = u[j]
      i = i + max(1, j - k) 
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("", ""),
    ("world", ""),
    ("hello", "ll"),
    ("aaaaa", "ab"),
    ("aaaaaaaaaab", "aaaaab"),
    ("abababababababababababca", "ababababca"),
    ("mississippi", "issi"),
  ]
  rslts = [solver.strStr(s, pattern) for s, pattern in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")