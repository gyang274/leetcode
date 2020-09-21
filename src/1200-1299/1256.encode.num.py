class Solution:
  def encode(self, num: int) -> str:
    # encode: at i-th least signficant digit, 1 << i if 1 else 1 << (i - 1)
    # so, "01101" = (1 << (5 - 1)) + (1 << 4) + (1 << 3) + (1 << (2 - 1)) + (1 << 1)
    s = ""
    while num:
      if num & 1:
        s += "0"
      else:
        s += "1"
        num -= 2
      num >>= 1
    return s[::-1]

class Solution:
  def encode(self, num: int) -> str:
    return bin(num + 1)[3:]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    0, 1, 2, 3, 5, 8, 23, 42, 85,
  ]
  rslts = [solver.encode(num) for num in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
