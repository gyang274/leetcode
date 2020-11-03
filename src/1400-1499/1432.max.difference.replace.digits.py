class Solution:
  def xmax(self, num):
    x, s = list(map(int, str(num))), None
    for i in range(len(x)):
      if s is None:
        if x[i] < 9:
          s = x[i]
          x[i] = 9
      else:
        if x[i] == s:
          x[i] = 9
    return int(''.join(map(str, x)))
  def xmin(self, num):
    x, s = list(map(int, str(num))), None
    if x[0] == 1:
      for i in range(1, len(x)):
        if s is None:
          if x[i] > 1:
            s = x[i]
            x[i] = 0
        else:
          if x[i] == s:
            x[i] = 0
    else:
      s = x[0]
      x[0] = 1
      for i in range(1, len(x)):
        if x[i] == s:
          x[i] = 1
    return int(''.join(map(str, x)))
  def maxDiff(self, num: int) -> int:
    return self.xmax(num) - self.xmin(num)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    111111,
    555555,
    999999,
    142857,
    285714,
    914085,
  ]
  rslts = [solver.maxDiff(num) for num in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
