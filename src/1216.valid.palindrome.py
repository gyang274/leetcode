class Solution:
  def recursive(self, i: int, j: int) -> int:
    # min num of deletions to make self.s palindrome
    if (i, j) not in self.memo:
      if i + 1 > j:
        self.memo[(i, j)] = 0
      elif self.s[i] == self.s[j]:
        self.memo[(i, j)] = self.recursive(i + 1, j - 1)
      else:
        self.memo[(i, j)] = min(self.recursive(i + 1, j), self.recursive(i, j - 1)) + 1
      # note: could early break whenever seen > k to make it more efficient, use raise to surrogate break.
    return self.memo[(i, j)]
  def isValidPalindrome(self, s: str, k: int) -> bool:
    self.s, self.memo = s, {}
    return self.recursive(0, len(s) - 1) <= k

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("abcdeca", 2),
    ("bacabaaa", 2),
  ]
  rslts = [solver.isValidPalindrome(s, k) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
