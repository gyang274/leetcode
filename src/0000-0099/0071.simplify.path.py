class Solution:
  def simplifyPath(self, path: str) -> str:
    p = path.split('/')
    q = []
    while p:
      x = p.pop(0)
      if x == '' or x == '.':
        continue
      elif x == '..':
        if len(q) > 0:
          q.pop(-1)
      else:
        q.append(x)
    return '/' + '/'.join(q)


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    "/home/",
    "/../",
    "/home//foo/",
    "/a/./b/../../c/",
    "/a/../../b/../c//.//",
    "/a//b////c/d//././/..",
  ]
  rslts = [solver.simplifyPath(path) for path in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")