class Solution:
  def addBinary(self, a: str, b: str) -> str:
    m, n = len(a), len(b)
    if m < n:
      m, n, a, b = n, m, b, a
    x, z, i = list(a), "0", -1
    while i >= -n:
      if a[i] == b[i] == "1":
        if z == "0":
          x[i], z = "0", "1"
      elif a[i] == "1":
        if z == "1":
          x[i] = "0"
      else:
        if z == "0":
          x[i] = b[i]
        else:
          x[i], z = ("1", "0") if b[i] == "0" else ("0", "1")
      i -= 1
    while i >= -m:
      if a[i] == z == "1":
        x[i] = "0"
      else:
        if not a[i] == z == "0":
          x[i], z = "1", "0"
        break
      i -= 1
    if z == "1":
      x = ["1"] + x
    return ''.join(x)


class Solution:
  def addBinary(self, a: str, b: str) -> str:
    x, y = int(a, 2), int(b, 2)
    while y:
      ansr = x ^ y
      carr = (x & y) << 1
      x, y = ansr, carr
    return bin(x)[2:] 


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ("0", "0"),
    ("0", "1"),
    ("1", "1"),
    ("1", "11"),
    ("10", "11"),
    ("1010", "1011"),
  ]
  rslts = [solver.addBinary(a, b) for a, b in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")