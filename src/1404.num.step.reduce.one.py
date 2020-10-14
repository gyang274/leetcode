class Solution:
  def numSteps(self, s: str) -> int:
    k, x = 0, 0
    while not ((s == '1' and k == 0) or (s == '' and k == 1)):
      if s[-1] == '0':
        if k == 1:
          x += 2
        else:
          x += 1
        s = s[:-1]
      else:
        if k == 1:
          x += 1
        else:
          x += 2
          k += 1
        s = s[:-1]
    return x

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "1",
    "10",
    "11",
    "1101",
  ]
  rslts = [solver.numSteps(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
