from typing import List

class Solution:
  def backtrack(self, s):
    if s not in self.memo:
      if s in self.wordDict:
        self.memo[s] = True
      else:
        self.memo[s] = False
        for i in range(1, len(s)):
          if s[:i] in self.wordDict and self.backtrack(s[i:]):
            self.memo[s] = True
            break
    return self.memo[s]
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    """backtrack
    """
    # memorize all seen combinations
    self.wordDict, self.memo = set(wordDict), {}
    return self.backtrack(s)

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ("leetcode", ["leet", "code"]),
    ("applepenapple", ["apple", "pen"]),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"]),
  ]
  rslts = [solver.wordBreak(s,wordDict) for s, wordDict in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}") 