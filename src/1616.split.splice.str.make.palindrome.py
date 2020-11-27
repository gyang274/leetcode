class Solution:
  def isPalindrome(self, s: str) -> bool:
    n = len(s)
    if n & 1:
      x, m, y = s[:(n // 2)], s[n // 2], s[(n // 2 + 1):]
    else:
      x, y = s[:(n // 2)], s[(n // 2):]
    return x[::-1] == y
  def checkPalindromeFormation(self, a: str, b: str) -> bool:
    n = len(a)
    # TC: O(N), SC: O(1).
    i = 0
    while i < n // 2:
      if a[i] == b[n - 1 - i]:
        i += 1
      else:
        break
    if i == n // 2 or self.isPalindrome(a[i:(n - i)]) or self.isPalindrome(b[i:(n - i)]):
      return True
    j = 0
    while j < n // 2:
      if b[j] == a[n - 1 - j]:
        j += 1
      else:
        break
    if j == n // 2 or self.isPalindrome(b[j:(n - j)]) or self.isPalindrome(a[j:(n - j)]):
      return True
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("x", "y"),
    ("abdef", "fecab"),
    ("xbdef", "xecab"),
    ("ulacfd", "jizalu"),
    ("pvhmupgqeltozftlmfjjde", "yjgpzbezspnnpszebzmhvp"),
  ]
  rslts = [solver.checkPalindromeFormation(a, b) for a, b in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
