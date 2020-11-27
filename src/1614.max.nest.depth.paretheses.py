class Solution:
  def maxDepth(self, s: str) -> int:
    d, m = 0, 0
    for x in s:
      if x == '(':
        d += 1
        m = max(m, d)
      elif x == ')':
        d -= 1
    return m

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "1",
    "1+(2*3)/(2-1)",
    "(1)+((2))+(((3)))",
    "(1+(2*3)+((8)/4))+1",
  ]
  rslts = [solver.maxDepth(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
