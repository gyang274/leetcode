class Solution:
  def rotateString(self, A: str, B: str) -> bool:
    """B is rotate of A <=> B is substr of A + A
    """
    return len(A) == len(B) and B in A + A

class Solution:
  def rotateString(self, A: str, B: str) -> bool:
    """Knuth-Morris-Pratt (KMP) Algorithm.
    """
    if not len(A) == len(B):
      return False
    s, p = A + A, B
    n, m = len(s), len(p)
    # corner case
    if m == 0: return 0
    # construct the \pi reference table
    u = [-1 for _ in range(m + 1)]
    k = -1
    for i in range(1, m + 1):
      while k >= 0 and B[k] != B[i - 1]:
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
          return True
      k = u[j]
      i = i + max(1, j - k) 
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("abcde", "cdeab"),
    ("abcde", "abced"),
  ]
  rslts = [solver.rotateString(A, B) for A, B in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")