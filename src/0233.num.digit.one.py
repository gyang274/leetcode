import math

class Solution:
  def countDigitOne(self, n: int) -> int:
    count, k = 0, 1
    while n > k - 1:
      # number of 1 at k-th position, module + residuals 
      count += n // (10 * k) * k + min(max(0, n % (10 * k) - k + 1), k)
      k *= 10
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    0,
    1,
    2,
    10,
    11,
    21,
    42,
    100,
    101,
    111,
    128,
    412,
    1008,
    1085,
    1587,
    2642,
  ]
  rslts = [solver.countDigitOne(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")