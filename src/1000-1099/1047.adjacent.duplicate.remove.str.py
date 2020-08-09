class Solution:
  def removeDuplicates(self, S: str) -> str:
    stack = []
    for x in S:
      if stack and stack[-1] == x:
        stack.pop()
      else:
        stack.append(x)
    return ''.join(stack)

from functools import reduce

class Solution:
  def removeDuplicates(self, S: str) -> str:
    return reduce(lambda x, s: x[:-1] if x[-1:] == s else x + s, S)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "abbaca",
  ]
  rslts = [solver.removeDuplicates(S) for S in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
