class Solution:
  def intToRoman(self, num: int) -> str:
    i2r = [
      (1000, "M"),
      (900, "CM"),
      (500, "D"),
      (400, "CD"),
      (100, "C"),
      (90, "XC"),
      (50, "L"),
      (40, "XL"),
      (10, "X"),
      (9, "IX"),
      (5, "V"),
      (4, "IV"),
      (1, "I")
    ]
    s = ''
    for (vi, vr) in i2r:
      s += (num//vi) * vr
      num %= vi
    return s

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    3,
    4,
    9,
    58,
  ]
  rslts = [
    solver.intToRoman(s) for s in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")