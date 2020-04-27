class Solution:
  def _valid(self, s):
    i, j = 0, len(s) - 1
    while i < j:
      if s[i] == s[j]:
        i += 1
        j -= 1
      else:
        return False
    return True
  def validPalindrome(self, s: str) -> bool:
    i, j = 0, len(s) - 1
    while i < j:
      if s[i] == s[j]:
        i += 1
        j -= 1
      else:
        if self._valid(s[(i + 1):(j + 1)]) or self._valid(s[i:j]):
          return True
        else:
          return False
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "aba",
    "abda",
    "abcda",
  ]
  rslts = [solver.validPalindrome(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")