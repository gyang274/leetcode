class Solution:
  def integerBreak(self, n: int) -> int:
    """all 3, until <= 4
      2 -> 1 + 1 -> 1, 
      3 -> 2 + 1 -> 2, 
      4 -> 2 + 2 -> 4,
      5 -> 3 + 2 -> 6,
      6 -> 3 + 3 -> 9,
      7 -> 3 + 4 -> 12,
      8 -> 3 + 3 + 2 -> 18, ...
    """
    if n < 5:
      x = {2: 1, 3: 2, 4: 4}
      return x[n]
    else:
      q, r = n // 3, n % 3
      if r < 2:
        q, r = q - 1, r + 3
      return (3 ** q) * r

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2, 3, 5, 8, 13, 21, 34, 55,
  ]
  rslts = [solver.integerBreak(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")