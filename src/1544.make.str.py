class Solution:
  def makeGood(self, s: str) -> str:
    stack = []
    for x in s:
      if stack and stack[-1].lower() == x.lower() and ord(stack[-1]) != ord(x):
        stack.pop()
      else:
        stack.append(x)
    return ''.join(stack)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "abBAcC",
    "leEeetcode",
  ]
  rslts = [solver.makeGood(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
