class Solution:
  def repeatedSubstringPattern(self, s: str) -> bool:
    n = len(s)
    for i in range(1, n // 2 + 1):
      if n % i == 0 and s[0:i] * (n // i) == s:
        return True
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "",
    "a",
    "aa",
    "abc",
    "ababab",
    "abcabcabcabc"
  ]
  rslts = [solver.repeatedSubstringPattern(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
    