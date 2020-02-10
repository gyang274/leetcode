from typing import List

class Solution:
  def backtrack(self, rslt: List[str], s: str) -> None:
    if len(s) == 0:
      self.ans.append(rslt)
    else:
      for i in range(1, len(s) + 1):
        if self.isPalindrome(s[:i]):
          self.backtrack(rslt + [s[:i]], s[i:])
  def isPalindrome(self, s: str) -> bool:
    if not s in self.memo:
      if len(s) <= 1:
        self.memo[s] = True
      else:
        self.memo[s] = (s[0] == s[-1]) and self.isPalindrome(s[1:-1])
    return self.memo[s]
  def partition(self, s: str) -> List[List[str]]:
    """backtrack/recurisve + memorization.
    """
    self.ans, self.memo = [], {}
    self.backtrack([], s)
    return self.ans

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    "",
    "a",
    "aa",
    "ab",
    "aab",
    "aba",
    "aabba",
    "aababa",
    "aabbaa",
  ]
  rslts = [solver.partition(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  
