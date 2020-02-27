from collections import defaultdict

class Solution:
  def canPermutePalindrome(self, s: str) -> bool:
    """At most one character showed odd number of times.
    """
    xdict = defaultdict(lambda: 0)
    for x in s:
      xdict[x] += 1
    counter = 0
    for x in xdict:
      # x % 2 == 1
      if xdict[x] & (-xdict[x]) == 1:
        counter += 1
        if counter > 1:
          return False
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "", "a", "ab", "aab", "leet", "code", "carerec",
  ]
  rslts = [solver.canPermutePalindrome(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")