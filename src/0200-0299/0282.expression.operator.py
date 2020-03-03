from typing import List
from collections import deque

class Solution:
  def _eval(self, stack, num):
    # process trailing "*"
    if stack and stack[-1] == "*":
      operator, operand = stack.pop(), stack.pop()
      stack.append(operand * int(num))
    else:
      stack.append(int(num))
    # process "+" and "-"
    x = stack.popleft()
    while stack:
      operator, y = stack.popleft(), stack.popleft()
      if operator == "+":
        x += y
      else:
        # operator == "-"
        x -= y
    return x
  def backtrack(self, prefix, stack, num, target) -> List[str]:
    """Args
      prefix: previous parsed num to expression.
      stack: unresolved operations, trailing with operator "+", "-", "*", 
        keep stack resolved as much as possible so that its at most "[[a+]b*]"
    """
    # check termination condiation
    if len(num) == 1 or not num[0] == "0":
      if self._eval(stack.copy(), num) == target:
        self.ans.append(prefix + num)
    # recursive
    if len(num) > 1:    
      n = 1 if num[0] == "0" else len(num) - 1
      # process trailing "*"
      if stack and stack[-1] == "*":
        operator, operand = stack.pop(), stack.pop()
      else:
        operator, operand = "*", 1
      for i in range(n):
        stackit = stack + deque([operand * int(num[:(i + 1)])])
        # "+"
        self.backtrack(
          prefix + num[:(i + 1)] + "+", stackit + deque(["+"]), num[(i + 1):], target
        )
        # "-"
        self.backtrack(
          prefix + num[:(i + 1)] + "-", stackit + deque(["-"]), num[(i + 1):], target
        )
        # "*"
        self.backtrack(
          prefix + num[:(i + 1)] + "*", stackit + deque(["*"]), num[(i + 1):], target
        )
  def addOperators(self, num: str, target: int) -> List[str]:
    """backtrack, pay attention to 0.
    """
    if num == "":
      return []
    self.ans = []
    self.backtrack("", deque([]), num, target)
    return self.ans

class Solution:
  def backtrack(self, i, prefix, prev, curr, value):
    """Keep track the last operation only, reverse back previous '+' and '-' for '*' appending.
    """
    if i == self.n:
      if value == self.target:
        self.ans.append(prefix)
      return None
    # build curr operand
    curr += self.num[i]
    # no operator, extend operand
    if i + 1 < self.n and not curr == "0":
      self.backtrack(i + 1, prefix, prev, curr, value)
    # init expression with operand
    if prefix == "":
      self.backtrack(i + 1, curr, curr, "", value + int(curr))
    # extd expresssion with operator and operand
    else:
      # "+"
      self.backtrack(i + 1, prefix + "+" + curr, curr, "", value + int(curr))
      # "-"
      self.backtrack(i + 1, prefix + "-" + curr, "-" + curr, "", value - int(curr))
      # "*"
      # reverse prev and calculate prev * curr precedence to "+" or "-"
      rev = int(prev) * int(curr)
      self.backtrack(i + 1, prefix + "*" + curr, str(rev), "", value - int(prev) + rev)
  def addOperators(self, num: str, target: int) -> List[str]:
    """backtrack, pay attention to 0.
    """
    self.num = num
    self.target = target
    self.n = len(num)
    self.ans = []
    self.backtrack(0, "", 0, "", 0)
    return self.ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("", 0),
    ("0", 0),
    ("00", 0),
    ("105", 5),
    ("123", 6),
    ("223", 8),
  ]
  rslts = [solver.addOperators(num, target) for num, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")