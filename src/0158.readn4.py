class Solution:
  def __init__(self):
    self.leftover = []
  def read(self, buf, n):
    # read from leftover
    x = len(self.leftover)
    if n < x:
      buf[:n], self.leftover = self.leftover[:n], self.leftover[n:]
      return n
    else:
      buf[:x], self.leftover = self.leftover, []
      # read more from file
      b = [' '] * 4
      while x < n:
        y = read4(b)
        buf[x:] = b
        x += y
        if y < 4:
          break
      if x > n:
        self.leftover = buf[n:x]
    return min(x, n)