class Solution:
  def integerReplacement(self, n: int) -> int:
    i = 0
    while n > 1:
      if n & 1:
        # ...11 then n + 1 -> ...00
        if n & 2 and n > 3:
          n += 1
        # ...01 then n - 1 -> ...00
        else:
          n -= 1
      else:
        n >>= 1 
      i += 1
    return i

if __name__ == '__main__':
  solver = Solution()
  cases = [
    1, 2, 3, 5, 8, 13, 23, 42, 85,
  ]
  rslts = [solver.integerReplacement(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")