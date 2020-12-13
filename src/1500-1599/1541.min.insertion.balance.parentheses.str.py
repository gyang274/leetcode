class Solution:
  def minInsertions(self, s: str) -> int:
    i, r, c = 0, 0, 0
    while i < len(s):
      if s[i] == '(':
        r += 1
        i += 1
      elif s[i:(i + 2)] == '))':
        r -= 1
        i += 2
      else:
        # ')('
        r -= 1
        c += 1
        i += 1
      if r < 0:
        r += 1
        c += 1
    return r * 2 + c

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "(()))",
    "(()))(()))()())))",
  ]
  rslts = [solver.minInsertions(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
