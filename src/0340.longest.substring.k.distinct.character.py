from collections import defaultdict

class Solution:
  def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
    i, j, l, w = 0, 0, 0, defaultdict(lambda: 0)
    while i <= j:
      if len(w) <= k and j < len(s):
        w[s[j]] += 1
        j += 1
        if len(w) <= k:
          l = max(l, j - i)
      else:
        if i < len(s):
          w[s[i]] -= 1
          if w[s[i]] == 0:
            w.pop(s[i])
        i += 1
    return l

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("aacbbbdabcd", 0),
    ("aacbbbdabcd", 1),
    ("aacbbbdabcd", 2),
  ]
  rslts = [solver.lengthOfLongestSubstringKDistinct(s, k) for s, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")