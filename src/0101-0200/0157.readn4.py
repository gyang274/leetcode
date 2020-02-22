class Solution:
  def read(self, buf, n):
    x, b = 0, [' '] * 4
    while x < n:
      y = read4(b)
      buf[x:] = b
      x += y
      if y < 4:
        break
    return min(x, n)

