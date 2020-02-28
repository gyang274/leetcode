from functools import reduce

class Solution:
  def titleToNumber(self, s: str) -> int:
    n = 0
    for x in s:
      n = n * 26 + ord(x) - 64
    return n

class Solution:
  def titleToNumber(self, s: str) -> int:
    return reduce(lambda x, y : x * 26 + y, [ord(c) - 64 for c in list(s)])


if __name__ == '__main__':
  solver = Solution()
  cases = [
    "A",
    "Z",
    "AA",
    "AZ",
    "ZY",
    "ZZ",
    "YGYF",
  ]
  rslts = [solver.titleToNumber(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")   