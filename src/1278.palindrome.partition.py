from functools import lru_cache

class Solution:
  @lru_cache(None)
  def numChangesToPalindrome(self, i, j):
    # num of changes to make s[i:j] to palindrome
    if i + 1 >= j:
      return 0
    return self.numChangesToPalindrome(i + 1, j - 1) + (0 if self.s[i] == self.s[j - 1] else 1)
  @lru_cache(None)
  def recursive(self, i, k):
    if k == 1:
      return self.numChangesToPalindrome(i, self.n)
    # num of change on s that can split s[i:] into k palindrome
    count = self.n
    for j in range(i + 1, self.n - (k - 1) + 1):
      count = min(count, self.numChangesToPalindrome(i, j) + self.recursive(j, k - 1))
    return count
  def palindromePartition(self, s: str, k: int) -> int:
    self.s, self.n = s, len(s)
    return self.recursive(0, k)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("abc", 2),
    ("abc", 3),
  ]
  rslts = [solver.palindromePartition(s, k) for s, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
