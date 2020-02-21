from collections import deque

class Solution:
  def _exec_md(self, stack, operand):
    """execute multiplication and division immediately.
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
    """execute plus and minus at the end of all parsed.
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
  def calculate(self, s: str) -> int:
    stack, operand = deque([]), 0
    for x in s:
      if x.isdigit():
        operand = operand * 10 + int(x)
      else:
        if x in {"+", "-", "*", "/"}:
          operand = self._exec_md(stack, operand)
          stack.append(x)
    operand = self._exec_md(stack, operand)
    return self._exec_pm(stack)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "0-0",
    " 3/2 ",
    "3+2*2",
    " 3 + 5 / 2",
  ]
  rslts = [solver.calculate(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  