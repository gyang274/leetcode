from typing import List

class Solution:
  def backtrack(self, sets, ans, s, ndot):
    if ndot == 0:
      if int(s) <= 255 and (len(s) == 1 or s[0] != '0'):
        sets.append(ans + [s])
    else:
      for i in range(1, 4):
        if int(s[:i]) <= 255 and (i == 1 or s[0] != '0') and (ndot <= len(s[i:]) <= 3 * ndot):
          self.backtrack(sets, ans + [s[:i]], s[i:], ndot - 1)
  def restoreIpAddresses(self, s: str) -> List[str]:
    if len(s) < 4: return []
    sets = []
    self.backtrack(sets, [], s, 3)
    rslt = ['.'.join(ans) for ans in sets] 
    return rslt

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    "0000",
    "00000",
    "1111111",
    "11111111",
    "25523255",
  ]
  rslts = [solver.restoreIpAddresses(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")