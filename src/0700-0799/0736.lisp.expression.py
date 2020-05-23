class Solution:
  def evaluate(self, expression: str) -> int:
    stack, d, tokens = [], {}, ['']
    def getval(token):
      return d.get(token, token)
    def _parse(tokens):
      if tokens[0] == 'add':
        return str(int(getval(tokens[1])) + int(getval(tokens[2])))
      elif tokens[0] == 'mult':
        return str(int(getval(tokens[1])) * int(getval(tokens[2])))
      else:
        # let
        for i in range(1, len(tokens) - 1, 2):
          if tokens[i + 1]:
            d[tokens[i]] = d.get(tokens[i + 1], tokens[i + 1])
        return d.get(tokens[-1], tokens[-1])
    for e in expression:
      if e == '(':
        # collect the let into dict
        if tokens[0] == 'let':
          _parse(tokens)
        # recreate d by dict(d) as dict outside 
        stack.append((tokens, dict(d)))
        tokens = ['']
      elif e == ')':
        rval = _parse(tokens)
        tokens, d = stack.pop()
        tokens[-1] += rval
      elif e == ' ':
        tokens.append('')
      else:
        tokens[-1] += e
    return int(tokens[-1])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "(add 1 2)",
    "(let x 3 x 2 x)",
    "(mult 3 (add 2 3))",
    "(let x 2 (mult x 5))",
    "(let a1 3 b2 (add a1 1) b2)",
    "(let x 1 y 2 x (add x y) (add x y))",
    "(let x 2 (add (let x 3 (let x 4 x)) x))",
    "(let x 2 (mult x (let x 3 y 4 (add x y))))",
  ]
  rslts = [solver.evaluate(expression) for expression in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
