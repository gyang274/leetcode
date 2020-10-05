from collections import defaultdict, deque

class Solution:
  def findTheLongestSubstring(self, s: str) -> int:
    # bitmask aeiou with xxxxx
    mask, seen, smax, vowels = 0, {0: -1}, 0, {x: 1 << i for i, x in enumerate('aeiou')}
    for i, x in enumerate(s):
      if x in vowels:
        mask ^= 1 << vowels[x]
      seen.setdefault(mask, i)
      smax = max(smax, i - seen[mask])
    return smax

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "bcbcbc",
    "leetcodeisgreat",
    "taergsiedocteel",
    "eleetminicoworoep",
  ]
  rslts = [solver.findTheLongestSubstring(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
