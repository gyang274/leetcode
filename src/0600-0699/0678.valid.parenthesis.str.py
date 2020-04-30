class Solution:
  def _valid(self, s, l, r):
    # count: ( - ), wcount: "*" available
    count, wcount = 0, 0
    for x in s:
      if x == l:
        count += 1
      elif x == r:
        if count > 0:
          count -= 1
        elif wcount > 0:
          wcount -= 1
        else:
          return False
      else:
        wcount += 1
    return wcount >= count
  def checkValidString(self, s: str) -> bool:
    return self._valid(s, "(", ")") and self._valid(s[::-1], ")", "(")

class Solution:
  def checkValidString(self, s: str) -> bool:
    # lo, hi: lower and upper bound of ")"
    lo = hi = 0
    for x in s:
      lo += 1 if x == "(" else -1
      hi += 1 if x != ")" else -1
      if hi < 0:
        return False
      lo = max(lo, 0)
    return lo == 0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "(*))",
    "(())((())()()(*)(*()(())())())()()((()())((()))(*",
  ]
  rslts = [solver.checkValidString(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
