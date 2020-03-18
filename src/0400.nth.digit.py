class Solution:
  def findNthDigit(self, n: int) -> int:
    k, nk = 1, 9
    while n > nk * k:
      n -= nk * k
      k += 1
      nk *= 10
    return str(10 ** (k - 1) + (n - 1) // k)[(n - 1) % k]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2, 3, 5, 8, 23, 42, 85,
  ]
  rslts = [solver.findNthDigit(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
