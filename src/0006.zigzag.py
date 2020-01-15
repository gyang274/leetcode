class Solution:
  def convert(self, s: str, numRows: int) -> str:
    l = len(s)
    if numRows <= 1 or numRows > l:
      return s
    k = 2 * (numRows - 1)
    x = ''
    for i in range(0, numRows):
      if i >= l:
        break
      x += s[i]
      j = 1
      if i == 0 or i == (numRows - 1):
        k = 2 * (numRows - 1)
        while i + k * j < l:
          x += s[i + k * j]
          j += 1
      else:
        ik = 2 * (numRows - 1  - i)
        while True:
          if i + k * (j - 1) + ik < l:
            x += s[i + k * (j - 1) + ik]
          else:
            break
          if i + k * j < l:
            x += s[i + k * j]
          else:
            break
          j += 1
    return x


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ("PAYPALISHIRING", 3),
    ("PAYPALISHIRING", 4),
    ("PAYPALISHIRING", 2),
  ]
  rslts = [solver.convert(s, numRows) for s, numRows in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
