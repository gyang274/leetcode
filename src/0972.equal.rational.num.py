from fractions import Fraction

class Solution:
  def convertRationalToFraction(self, s: str) -> Fraction:
    # s <IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)>
    if '.' in s:
      x, yz = s.split('.')
      if '(' in yz:
        y, z = yz[:-1].split('(')
        if y == '':
          return int(x) + Fraction(int(z), (10 ** len(y)) * (10 ** len(z) - 1))
        return int(x) + Fraction(int(y), 10 ** len(y)) + Fraction(int(z), (10 ** len(y)) * (10 ** len(z) - 1))
      else:
        if yz == '':
          return int(x)
        return int(x) + Fraction(int(yz), 10 ** len(yz))
    else:
      return int(s)
  def isRationalEqual(self, S: str, T: str) -> bool:
    return self.convertRationalToFraction(S) == self.convertRationalToFraction(T)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("0.9(9)", "1."),
    ("0.(25)", "0.2(52)"),
    ("0.16(6)", "0.166(666)"),
  ]
  rslts = [solver.isRationalEqual(S, T) for S, T in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
