from typing import List

class Solution:
  def maxDepthAfterSplit(self, seq: str) -> List[int]:
    # depth of seq itself
    d, m = 0, 0
    for x in seq:
      if x == "(":
        d += 1
        m = max(m, d)
      else:
        d -= 1
    # split upto (m + 1) // 2
    m = (m + 1) // 2
    # assign to 0 aggressively
    ans, dA, dB = [0] * len(seq), 0, 0
    for i, x in enumerate(seq):
      if x =='(':
        if dA < m:
          dA += 1
        else:
          dB += 1
          ans[i] = 1
      else:
        # x == ')'
        if dB > 0:
          dB -= 1
          ans[i] = 1
        else:
          dA -= 1
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "(()())",
    "()(())",
    "((()))",
  ]
  rslts = [solver.maxDepthAfterSplit(seq) for seq in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
