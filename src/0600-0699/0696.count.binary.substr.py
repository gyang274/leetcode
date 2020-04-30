class Solution:
  def countBinarySubstrings(self, s):
    ans, prev, curr = 0, 0, 1
    for i in range(1, len(s)):
      if s[i - 1] != s[i]:
        ans += min(prev, curr)
        prev, curr = curr, 1
      else:
        curr += 1
    return ans + min(prev, curr)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "010110",
  ]
  rslts = [solver.countBinarySubstrings(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
