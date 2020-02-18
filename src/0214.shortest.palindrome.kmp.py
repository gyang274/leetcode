class Solution:
  def shortestPalindrome(self, s: str) -> str:
    """naive brute force.
    """
    n, r = len(s), s[::-1]
    i = n
    while i > 0:
      if s[:i] == r[(n - i):]:
        break
      i -= 1
    return r[:(n - i)] + s

class Solution:
  def shortestPalindrome(self, s: str) -> str:
    """Q0028: Knuth-Morris-Pratt (KMP) Algorithm.
    """
    # corner case
    n = len(s)
    # if n == 0:
    #   return ""
    # reversed s
    r = s[::-1]
    # construct the \pi reference table of p = s + '#' + r, r = s[::-1]
    p = s + '#' + r
    # kmp essential
    u = [-1 for _ in range(len(p) + 1)]
    k = -1
    for i in range(1, len(p) + 1):
      while k >= 0 and p[k] != p[i - 1]:
        k = u[k]
      k += 1
      u[i] = k
    # construct shortest palindrome from s based on p's kmp \pi table
    # u[-1] == argmax_i(r[(n - i):] == s[:i])
    return r[:(n - u[-1])] + s

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "",
    "a",
    "aa",
    "ab",
    "aba",
    "aab",
    "abc",
    "abcd",
    "abababa",
    "aabcdaa",
    "aacecaaa",
    "cacacabc",
  ]
  rslts = [solver.shortestPalindrome(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")