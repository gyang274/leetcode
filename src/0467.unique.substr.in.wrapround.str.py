class Solution:
  def findSubstringInWraproundString(self, p: str) -> int:
    """count of unique substr ended with x is determined by max length ended with character x
    """
    ans = {x: 1 for x in p}
    i, l = 1, 1
    while i < len(p):
      if (ord(p[i]) - ord(p[i - 1])) % 26 == 1:
        l += 1
        ans[p[i]] = max(ans[p[i]], l)
      else:
        l = 1
      i += 1
    return sum(ans.values())

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "a",
    "zab",
    "zabcdefghijklmnopqrstuvwxyz",
  ]
  rslts = [solver.findSubstringInWraproundString(p) for p in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")