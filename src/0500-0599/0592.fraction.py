class Solution:
  def _getGCD(self, x, y):
    while y:
      x, y = y, x % y
    return x
  def _getLCM(self, x, y):
    return x * y // self._getGCD(x, y)
  def _add(self, x1, x2):
    x1n, x1d = [int(s) for s in x1.split("/")]
    x2n, x2d = [int(s) for s in x2.split("/")]
    xd = self._getLCM(x1d, x2d)
    xn = x1n * (xd // x1d) + x2n * (xd // x2d)
    dd = self._getGCD(xn, xd)
    return str(xn // dd) + "/" + str(xd // dd)
  def fractionAddition(self, expression: str) -> str:
    i, n = 0, len(expression)
    x, z = "0/1", ""
    for i in range(n):
      e = expression[i] 
      if e == "-" or e == "+":
        if z:
          x = self._add(x, z)
          z = ""
        if e == "-":
          z += e
      else:
        z += e  
    x = self._add(x, z)
    return x

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "-1/2+1/2",
    "-1/2+1/2+1/3",
    "1/2-1/3",
    "1/3-1/2",
  ]
  rslts = [solver.fractionAddition(expression) for expression in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
