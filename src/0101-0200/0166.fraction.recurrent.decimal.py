class Solution:
  def fractionToDecimal(self, numerator: int, denominator: int) -> str:
    """fraction recurrence: all prime except 2 and 5 cause recurrence, how many digits?
      since 1/9 = 0.(1), 1/99 = 0.(01), 1/999 = (0.001), so 1/99...9 determines number of digits and convert the
      fractional expression say 2/7 = 285714/999999 = 0.(285714)
      so how about non-recurrence part? say, convert to 9...90...0, number of 0 determines non-recurrence leading,
      and convert 3/14 = 2142855/9999990 = 0.2(142857), note 142857 = 142855+2
    """
    if denominator == 0:
      return None
    negative = False
    if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
      negative = True
    # -2147483648 overflow?
    numerator = abs(numerator)
    denominator = abs(denominator)
    # integer part
    z = 0
    if numerator > denominator:
      z = numerator // denominator
      numerator -= z * denominator
    z = ('-' if negative else '') + str(z)
    if numerator == 0:
      return z
    # fractional part
    reminders = {}
    f, i, r = '', 0, numerator * 10
    while not r in reminders:
      q = r // denominator
      reminders[r] = (i, q)
      f += str(q)
      r = r % denominator * 10
      i += 1
    s = reminders[r][0]
    return z + '.' + f[:s] + ('' if r == 0 else '(' + f[s:] + ')')

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (1, 2),
    (1, 3),
    (1, 5),
    (1, 7),
    (1, 8),
    (1, 70),
    (1, 72),
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