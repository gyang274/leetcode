class Solution:
  def thousandSeparator(self, n: int) -> str:
    if n == 0:
      return '0'
    s = ''
    while n:
      s = (f'{n % 1000:03d}' if n > 999 else str(n % 1000)) + '.' + s
      n //= 1000
    return s[:-1]

class Solution:
  def thousandSeparator(self, n: int) -> str:
    return f'{n:,}'.replace(',', '.')

if __name__ == '__main__':
  solver = Solution()
  cases = [
    0, 1, 123, 2134, 51040,
  ]
  rslts = [solver.thousandSeparator(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
