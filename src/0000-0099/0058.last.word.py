class Solution:
  def lengthOfLastWord(self, s: str) -> int:
    x, y = 0, False
    for z in reversed(s):
      if z == ' ':
        if y: break
      else:
        y = True
        x += 1
    return x


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    "",
    "Hello",
    "Hello ",
    "Hello World",
    "Hello World ",
  ]
  rslts = [solver.lengthOfLastWord(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")