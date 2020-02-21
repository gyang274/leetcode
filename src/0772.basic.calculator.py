from collections import deque

class Solution:
  def __init__(self):
    # signs
    self.signs = {"+", "-", "*", "/"}
    # self.signs_md = {"*", "/"}
    # self.signs_pm = {"+", "-"}
  def _exec_md(self, stack, operand):
    """execute multiplication and division immediately, in-place stack and running operand from right.
    """
    if stack and stack[-1] in {'*', '/'}:
      operator, v = stack.pop(), stack.pop()
      if operator == "*":
        stack.append(v * operand)
      else:
        stack.append(v // operand)
    else:
      stack.append(operand)
    return 0
  def _exec_pm(self, stack):
    """execute plus and minus at the end of all parsed, in-place stack and running rslt from left.
    """
    rslt = stack.popleft()
    while stack:
      operator, operand = stack.popleft(), stack.popleft()
      if operator == "+":
        rslt += operand
      else:
        # operator == "-"
        rslt -= operand
    return rslt
  def _calculate(self) -> int:
    # recursive within each parethesis
    stack, operand = deque([]), 0
    while self.i < self.n:
      x = self.s[self.i]
      if x.isdigit():
        operand = operand * 10 + int(x)
      else:
        # push sign or recusrive over parethesis accordingly
        if x in self.signs:
          # execution * or / of stacked[-1] operator immediately before push new operator
          operand = self._exec_md(stack, operand)
          stack.append(x)
        elif x == "(":
          self.i += 1
          # recursive over ()
          operand = self._calculate()
        elif x == ")":
          # settle the reursion and return back to upper level
          operand = self._exec_md(stack, operand)
          return self._exec_pm(stack)
      # print(f"proc: {self.s=}, {self.i=}, {x=}, {operand=}, {stack=}")
      self.i += 1
    operand = self._exec_md(stack, operand)
    return self._exec_pm(stack)
  def calculate(self, s: str) -> int:
    """Q0224 + Q0227, recursive over each ().
    """
    self.s, self.i, self.n = s, 0, len(s)
    return self._calculate()

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "0-0",
    " 3/2 ",
    "3+2*2",
    " 1 + 1 ",
    " 3+5 / 2",
    " 7 - 4 / 2 ",
    "2*(5+5*2)/3+(6/2+8)",
    "(2+6* 3+5- (3*14/7+2)*5)+3",
  ]
  rslts = [solver.calculate(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}") 