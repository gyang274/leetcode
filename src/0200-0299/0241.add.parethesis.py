from typing import List

class Solution:
  def parseInput(self, input: str) -> List:
    operand, stack = 0, []
    for x in input:
      if x.isdigit():
        operand = operand * 10 + int(x)
      else:
        stack.append(operand)
        stack.append(x)
        operand = 0
    stack.append(operand)
    return stack
  def calculate(self, l, r) -> List[int]:
    if (l, r) not in self.memo:
      if l == r:
        self.memo[(l, r)] = [self.stack[r]]
      else:
        ans = []
        # number of operators
        n = (r - l) // 2
        # pivot through each opeator as the last one to execute, add parethesis around (left) and (right)
        for k in range(n):
          # print(f"{l=}, {r=}, {k=}, {self.stack[2 * k + 1]=}")
          for xl in self.calculate(l, l + 2 * k):
            for xr in self.calculate(l + 2 * k + 2, r):
              if self.stack[l + 2 * k + 1] == "+":
                ans.append(xl + xr)
              elif self.stack[l + 2 * k + 1] == "-":
                ans.append(xl - xr)
              elif self.stack[l + 2 * k + 1] == "*":
                ans.append(xl * xr)
              else:
                raise("Invalid operator.")
        self.memo[(l, r)] = ans
    # print(f"{l=}, {r=}, {self.memo[(l, r)]=}")
    return self.memo[(l, r)]
  def diffWaysToCompute(self, input: str) -> List[int]:
    """Catalan Number, refr. Q0022, Q0095. C_0 = 1, C_n = sum_i C_i C_{n-1-i}, i = 0, .., n-1
    """
    # parse input into list of operand and operators
    self.stack = self.parseInput(input)
    self.memo = {}
    return self.calculate(0, len(self.stack) - 1)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "",
    "1",
    "1+1",
    "2-1-1",
    "2*3-4*5",
    "2+3-4*5+6-7*8+9",
  ]
  rslts = [solver.diffWaysToCompute(input) for input in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")