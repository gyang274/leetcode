class Solution:
  def calPoints(self, ops: List[str]) -> int:
    stack = []
    for s in ops:
      if s == "C":
        stack.pop()
      elif s == "D":
        stack.append(stack[-1] * 2)
      elif s == "+":
        stack.append(stack[-2] + stack[-1])
      else:
        stack.append(int(s))
    return sum(stack)