class Solution:
  # def canWinSegment(self, n):
  #   """if start with all "+", say "+" * n, then can win if not both n - 2 or n - 3 can win, 
  #     since one flip can block 2 or 3 from side, initialized with 0, 1 False, 2, 3, 4 True. 
  #   """
  #     # canWin on a segment of n consecutive "+"
  #     return not (n == 0 or n % 4 == 1)
  def canWin(self, s: str) -> bool:
    """parse into segment of consecutive "+", notice there are 3 different type segment
      1) "+" * 4, 1st player can force to win or loss anyway wanted
      2) "+" * n, where not (n == 0 or n == 4 or n % 4 == 1), 1st player can win if play appropriately
      3) "+" * n, where n == 0 or n % 4 == 1, 1st cann't win anyway
      Thus, canWin if any of following conditions satisfied:
      1) odd number of segment "+" * 4, since we can change canWin status accordingly.
      2) even number of segment "+" * 4, odd number of segment "+" * n, where not (n == 0 or n == 4 or n % 4 == 1).
        Under 2) we use the odd number of other canWin segment to force our opponent start one of the segment "+" * 4,
        so that we have odd number of "+" * 4 to adjust the status anyway we want.
    """
    # n: number of consecutive "+" on a current segment, reset everytime see a "-"
    # n4: number of segment "+" * 4, nW: number of segment "+" * n that canWin by itself.
    n, n4, nW = 0, 0, 0
    for x in s:
      if x == "+":
        n += 1
      else:
        if n == 4:
          n4 += 1
        elif not (n == 0 or n % 4 == 1):
          nW += 1
        n = 0
    # the last segment "...++"
    if n == 4:
      n4 += 1
    elif not (n == 0 or n % 4 == 1):
      nW += 1
    return (n4 & (-n4) == 1) or (nW & (-nW) == 1)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "",
    "+",
    "++",
    "+++",
    "++++",
    "+++++",
    "++++-+++",
    "++++-+++-+++",
    "++++-++++",
    "++++-++++-+++",
    "++++-++++-++++",
  ]
  rslts = [solver.canWin(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")