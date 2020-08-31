import math

class Solution:
  def numPrimeArrangements(self, n: int) -> int:
    # num of primes <= n
    x = [1] * (n + 1)
    x[0], x[1] = 0, 0
    for k in range(2, min(int(n ** 0.5) + 2, n)):
      if x[k]:
        for i in range(k * 2, n + 1, k):
          x[i] = 0
    s = sum(x)
    return math.factorial(s) * math.factorial(n - s) % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    1, 1, 2, 3, 5, 8, 23, 42, 85, 100,
  ]
  rslts = [solver.numPrimeArrangements(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
