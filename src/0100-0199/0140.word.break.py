from typing import List

class Solution:
  def backtrack(self, s):
    if s not in self.memo:
      self.memo[s] = []
      for i in range(1, len(s)):
        if s[:i] in self.wordDict:
          splits = self.backtrack(s[i:])
          for split in splits:
            self.memo[s].append(s[:i] + " " + split)
      if s in self.wordDict:
        self.memo[s].append(s)
    return self.memo[s]
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    """backtrack
    """
    # memorize all seen combinations
    self.wordDict, self.memo = set(wordDict), {}
    self.backtrack(s)
    return self.memo[s]

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ("leetcode", ["leet", "code"]),
    ("applepenapple", ["apple", "pen"]),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"]),
    ("catsanddog", ["cats", "dog", "sand", "and", "cat"]),
    ("aaaaaaa", ["aaaa","aa","a"])
  ]
  rslts = [solver.wordBreak(s,wordDict) for s, wordDict in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}") 