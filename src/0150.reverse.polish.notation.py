from typing import List

class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
    stack, operators = [], set(['+', '-', '*', '/'])
    for x in tokens:
      if x in operators:
        n1, n2 = stack.pop(), stack.pop()
        stack.append(str(int(eval(n2 + x + n1))))
      else:
        stack.append(x)
    return int(stack[0])


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ["2","1","+","3","*"],
    ["4", "13", "5", "/", "+"],
    ["4","-2","/","2","-3","-","-"],
    ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
  ]
  rslts = [solver.evalRPN(tokens) for tokens in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  