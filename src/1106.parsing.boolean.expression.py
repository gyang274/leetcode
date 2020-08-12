class Solution:
  def parseBoolExpr(self, expression: str) -> bool:
    operators = {'!', '&', '|'}
    # stack
    # currO: current operator
    # currB, currB: current boolean and boolean list
    stack, currO, currB, currBS = [], '', None, []
    for x in expression:
      if x in operators:
        currO = x
      elif x == 't':
        currB = True
      elif x == 'f':
        currB = False
      elif x == '(':
        stack.append(currBS)
        currBS = []
        stack.append(currO)
        currO = ''
      elif x == ')':
        currBS.append(currB)
        prevO = stack.pop()
        if prevO == '&':
          currB = all(currBS)
        elif prevO == '|':
          currB = any(currBS)
        else:
          # prevO == '!'
          currB = not currBS[0]
        currBS = stack.pop()
        currBS.append(currB)
      else:
        # x == ','
        currBS.append(currB)
    return currB

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "f",
    "!(f)",
    "|(f,t)",
    "&(t,f)",
    "|(&(t,f,t),!(t))",
    "|(&(t,!(t),t),|(f,!(f)))",
  ]
  rslts = [solver.parseBoolExpr(expression) for expression in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
