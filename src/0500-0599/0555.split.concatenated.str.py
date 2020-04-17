from typing import List

class Solution:
  def splitLoopedString(self, strs: List[str]) -> str:
    """brute force
    """
    n = len(strs)
    # s: concatenated string without loop and split,
    # b: breaking points for each components in strs
    s, b = "", [0]    
    for i in range(n):
      strs[i] = max(strs[i], strs[i][::-1])
      s += strs[i]
      b.append(len(strs[i]))
      b[i + 1] += b[i]
    # brute force to check all kinds of split..
    smax = s
    for i in range(n):
      si, ri = strs[i], strs[i][::-1]
      for k in range(len(si)):
        smax = max(
          smax, si[k:] + s[b[i+1]:] + s[:b[i]] + si[:k], ri[k:] + s[b[i+1]:] + s[:b[i]] + ri[:k]
        )
    return smax

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["abc", "xyz"],
    ["z", "z", "a", "zy"],
  ]
  rslts = [solver.splitLoopedString(strs) for strs in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
