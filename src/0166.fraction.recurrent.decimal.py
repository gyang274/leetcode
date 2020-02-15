class Solution:
  def fractionToDecimal(self, numerator: int, denominator: int) -> str:
    """fraction recurrence: all prime except 2 and 5 cause recurrence, how many digits?
      since 1/9 = 0.(1), 1/99 = 0.(01), 1/999 = (0.001), so 1/99...9 determines number of digits
      and convert fractional expression say 2/7 = 285714/999999 = 0.(285714)
    """


if __name__ == '__main__':
  solver = Solution()
  cases = [
    (1, 2),
    (1, 3),
    (1, 5),
    (1, 7),
    (1, 8),
    (2, 8),
    (0, 1),
    (1, 0),
    (-1, 4),
    (-1, -4),
    # beaware of overflow when cast negative to positive
    (-2147483648, -1),
  ]
  rslts = [solver.fractionToDecimal(numerator, denominator) for numerator, denominator in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  