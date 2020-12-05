from functools import lru_cache

class Solution:
  def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
    # dp, dynamic programming, only state of last n cells required for iteration.
    nm = n * m
    # make n smaller so recusive efficiently
    n, m = sorted([n, m])
    # mask: all 1s with n-bits
    mask = (1 << n) - 1
    # imask: encode the last n cells occupied by introvert or not
    # emask: enocde the last n cells occupied by extrovert or not
    imask = 0
    emask = 0
    # dp
    @lru_cache(None)
    def recursive(i, imask, emask, icount, ecount):
      # i: index of current cells
      # imask: mask of introvert in last n cells
      # emask: mask of extrovert in last n cells
      # icount: num of introvert available
      # ecount: num of extroverr available
      if i == nm or icount == ecount == 0:
        return 0
      # option: move on as empty cell
      maxscore = recursive(i + 1, mask & (imask << 1), mask & (emask << 1), icount, ecount)
      # leftr cell has lived intro/extro
      li, le = imask & 1, emask & 1
      # upper cell has lived intro/extro
      ui, ue = (imask >> (n - 1)) & 1, (emask >> (n - 1)) & 1
      # option: make an introvert live in cell
      if icount > 0:
        score = 120
        if i >= n and (not ui == ue == 0):
          score += -30 + (ui * -30 + ue * 20)
        if i % n != 0 and (not li == le == 0):
          score += -30 + (li * -30 + le * 20)
        maxscore = max(maxscore, score + recursive(i + 1, (mask & (imask << 1)) | 1, mask & (emask << 1), icount - 1, ecount))
      # option: mask an extrovert live in cell
      if ecount > 0:
        score = 40
        if i >= n and (not ui == ue == 0):
          score += 20 + (ui * -30 + ue * 20)
        if i % n != 0 and (not li == le == 0):
          score += 20 + (li * -30 + le * 20)
        maxscore = max(maxscore, score + recursive(i + 1, (mask & (imask << 1)), mask & (emask << 1) | 1, icount, ecount - 1))
      return maxscore
    return recursive(0, 0, 0, introvertsCount, extrovertsCount)
