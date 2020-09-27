class Solution:
  def removePalindromeSub(self, s: str) -> int:
    # 0 if empty, 1 if palindrome, 2 otherwise by removing all a then all b.
    if not s:
      return 0
    n = len(s)
    i, j = 0, n - 1
    while i < j:
      if s[i] == s[j]:
        i += 1
        j -= 1
      else:
        return 2
    return 1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "", "a", "ab",
  ]
  rslts = [solver.removePalindromeSub(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
