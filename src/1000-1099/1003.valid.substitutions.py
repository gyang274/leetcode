class Solution:
  def isValid(self, S: str) -> bool:
    # stack
    stack = []
    for s in S:
      if s == 'a':
        stack.append('a')
      elif stack and stack[-1] == 'a' and s == 'b':
        stack[-1] = 'b'
      elif stack and stack[-1] == 'b' and s == 'c':
        stack.pop()
      else:
        return False
    return not stack

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "aabcbc",
    "aabbcc",
    "cababc",
    "aabcbabcc"
  ]
  rslts = [solver.isValid(S) for S in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
