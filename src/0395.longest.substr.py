from collections import defaultdict

class Solution:
  def longestSubstring(self, s: str, k: int) -> int:
    # counter with index
    n, v = 0, defaultdict(list)
    for i, x in enumerate(s):
      v[x].append(i)
    # is s ok?
    w = [-1, len(s)]
    for x in v:
      if len(v[x]) < k:
        w.extend(v[x])
    # divide and conquer
    if len(w) > 2:
      w.sort()
      for i in range(len(w) - 1):
        n = max(n, self.longestSubstring(s[(w[i] + 1):w[i + 1]], k))
    else:
      return len(s)
    return n

class Solution:
  def longestSubstring(self, s, k):
    for c in set(s):
      if s.count(c) < k:
        return max(self.longestSubstring(t, k) for t in s.split(c))
    return len(s)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("ababbcd", 2),
    ("aaabbcc", 3),
  ]
  rslts = [solver.longestSubstring(s, k) for s, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
  