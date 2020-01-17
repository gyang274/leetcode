class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    maxLen = 0
    mstart = -1
    xdict = dict()
    for i, x in enumerate(s):
      if xdict.get(x, -1) > mstart:
        mstart = xdict[x]
      xdict[x] = i
      maxLen = max(maxLen, i - mstart)
    return maxLen


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    "", "abba", "abcabcbb", "bbbb", "b", "pwwkew"
  ]
  rslts = [solver.lengthOfLongestSubstring(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
        