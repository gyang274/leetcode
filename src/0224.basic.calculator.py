from collections import deque

class Solution:
  def __init__(self):
    # define digits
    self.digits = {"0","1","2","3","4","5","6","7","8","9"}
    # define signs
    self.signs = {"+","-"}
  def _exec(self, stack):
    while len(stack) > 2:
      x, operator, y = stack.popleft(), stack.popleft(), stack.popleft()
      if operator == "+":
        stack.appendleft(x + y)
      else:
        # operator == "-"
        stack.appendleft(x - y)
  def _calculate(self):
    # recursive within each parethesis
    x, stack = "", deque([])
    while self.i < self.n:
      r = self.s[self.i]
      if r == " ":
        pass
      elif r in self.digits:
        x += r
      else:
        # push x into stack
        if not x == "":
          stack.append(int(x))
          x = ""
        # push this sign or parethesis accordingly
        if r in self.signs:
          if not (stack and isinstance(stack[-1], int)):
            stack.append(0)
          stack.append(r)
        elif r == "(":
          self.i += 1
          stack.append(self._calculate())
        elif r == ")":
          self._exec(stack)
          return stack[0] if stack else 0
      # print(f"proc: {self.s=}, {self.i=}, {r=}, {x=}, {stack=}")
      self.i += 1
    if not x == "":
      stack.append(int(x))
      x = ""
    self._exec(stack)
    return stack[0] if stack else 0
  def calculate(self, s: str) -> int:
    """recursive over each ().
    """
    self.s, self.i, self.n = s, 0, len(s)
    return self._calculate()

class Solution:
  def calculate(self, s: str) -> int:
    """stack as the recursive calls, calculate immediately and keep one on-going result at each () level.
    """
    stack = []
    operand = 0
    rslt = 0 # the on-going result
    sign = 1 # 1 means positive, -1 means negative  
    for x in s:
      if x.isdigit():
        # build operand, since it could be more than one digit
        operand = operand * 10 + int(x)
      elif x == '+':
        # Evaluate the expression to the left, with result, sign, operand
        rslt += sign * operand
        # Save the recently encountered '+' sign
        sign = 1
        # Reset operand
        operand = 0
      elif x == '-':
        rslt += sign * operand
        sign = -1
        operand = 0
      elif x == '(':
        # Push the result and sign on to the stack, for later, push the result first, then sign
        stack.append(rslt)
        stack.append(sign)
        # Reset operand and result, as if new evaluation begins for the new sub-expression
        sign = 1
        rslt = 0
      elif x == ')':
        # Evaluate the expression to the left, with result, sign and operand
        rslt += sign * operand
        # ')' marks end of expression within a set of parenthesis
        # Its result is multiplied with sign on top of stack
        # as stack.pop() is the sign before the parenthesis
        rslt *= stack.pop() # stack pop 1, sign
        # Then add to the next operand on the top.
        # as stack.pop() is the result calculated before this parenthesis
        # (operand on stack) + (sign on stack * (result from parenthesis))
        rslt += stack.pop() # stack pop 2, operand
        # Reset the operand
        operand = 0
    return rslt + sign * operand

if __name__ == '__main__':
  solver = Solution()
  cases = [
    " ",
    " 0 ",
    " 1 ",
    " - 1 ",
    " 2 + ",
    "1 + 1",
    "- 1 + 1",
    " 2-1 + 2 ",
    " 2 + () - 1",
    "(1+(4+5+2)-3)+(6+8)",
    "- (1+(4+5+2)-3)+(6+8)",
  ]
  rslts = [solver.calculate(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  