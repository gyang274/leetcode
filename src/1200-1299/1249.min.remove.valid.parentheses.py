class Solution:
  def minRemoveToMakeValid(self, s: str) -> str:
    stack, r = [], ''
    for x in s:
      if x == '(':
        stack.append(r)
        r = ''
      elif x == ')':
        if stack:
          r = stack.pop() + '(' + r + ')'
      else:
        r += x
    return ''.join(stack) + r

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "()))(()",
    "a)b(c)d",
    "(a(b(c)d)",
    "lee(t(c)o)de)",
  ]
  rslts = [solver.minRemoveToMakeValid(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
