class Solution:
  def isValid(self, s: str) -> bool:
    isOpened = lambda x: x in set(("(", "[", "{"))
    # isClosed = lambda x: x in set((")", "]", "}"))
    isParied = lambda x, y: (x, y) == ("(", ")") or (x, y) == ("[", "]") or (x, y) == ("{", "}")
    z = []
    for x in s:
      if isOpened(x):
        z.append(x)
      else:
        if z:
          y = z.pop()
          if not isParied(y, x):
            return False
        else:
          return False
    if not z:
      return True
    else:
      return False


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    "()",
    "()[]{}",
    "({[]})",
    "(]",
    "([)]",
  ]
  rslts = [solver.isValid(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")