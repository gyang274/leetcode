class Solution:
  def lengthLongestPath(self, input: str) -> int:
    paths = input.split("\n")
    xmax, stack = 0, []
    for path in paths:
      level = 0
      while path[:1] == "\t":
        level += 1
        path = path[1:]
      while level < len(stack):
        stack.pop()
      stack.append(path)
      if "." in path:
        xmax = max(xmax, len('/'.join(stack)))
    return xmax

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "",
    "a",
    "dir\nanotherdir",
    "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext",
    "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext",
  ]
  rslts = [solver.lengthLongestPath(input) for input in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
