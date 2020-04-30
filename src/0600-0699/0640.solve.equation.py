class Solution:
  def parseOperand(self, stack, x):
    if x[-1] == "x":
      if x == "x" or x == "+x":
        stack[0] += 1
      elif x == "-x":
        stack[0] -= 1
      else:
        stack[0] += int(x[:-1])
    else:
      stack[1] += int(x)
  def parseEquation(self, equation):
    # parse equation lhs or rhs with +-[1-9]x
    x, stack = "", [0, 0]
    for i, e in enumerate(equation):
      if x and (e == "+" or e == "-"):
        self.parseOperand(stack, x)
        x = ""
      x += e
    self.parseOperand(stack, x)
    return stack
  def solveEquation(self, equation: str) -> str:
    lhs, rhs = [self.parseEquation(e) for e in equation.split("=")]
    b1 = lhs[0] - rhs[0]
    b0 = rhs[1] - lhs[1]
    if b1 == 0:
      if b0 == 0:
        return "Infinite solutions"
      else:
        return "No solution"
    return "x=" + str(b0 // b1)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "x=x",
    "x=x+2",
    "2x=3x",
    "-x=-1",
    "2x+3x-6x=x+2",
    "x+5-3+x=6+x-2",
  ]
  rslts = [solver.solveEquation(equation) for equation in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")

        