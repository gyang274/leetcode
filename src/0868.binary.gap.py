class Solution:
  def binaryGap(self, N: int) -> int:
    prev, curr, dist = -1, 0, 0
    while N > 0:
      if N & 1:
        if prev > -1:
          dist = max(dist, curr - prev)
        prev = curr
      N >>= 1
      curr += 1
    return dist
