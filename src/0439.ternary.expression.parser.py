class Solution:
  def parseTernary(self, expression: str) -> str:
    if len(expression) == 1:
      return expression
    i, q = 2, 1
    # split for True/False
    while q > 0:
      i += 1
      if expression[i] == "?":
        q += 1
      elif expression[i] == ":":
        q -= 1
    if expression[0] == "T":
      return self.parseTernary(expression[2:i])
    else:
      return self.parseTernary(expression[(i + 1):])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "T?2:3",
    "F?1:T?4:5",
    "T?T?F:5:2",
  ]
  rslts = [solver.parseTernary(expression) for expression in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
