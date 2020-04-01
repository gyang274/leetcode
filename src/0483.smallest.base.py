import math

class Solution:
  def smallestGoodBase(self, n: str) -> str:
    """math: O(logN)
      1 + b + .. + b^(k-1) = n => n = (b^k - 1) / (b - 1), smallest b <=> largest k
      - O(N) if try k = log2(n + 1), log3(2n + 1), .. for each b = 2, 3, ..., n-1
      - O(logN) if try solve b, f(b) = b^k - nb + (n - 1) = 0 for each k = int(log2(n + 1)), ..., 2
        b ~= log(n, k-1), newton's method, f'(b) = k * b^(k - 1) - n = 0, bnext = b - f(b) / f'(b).
        bnext = ((k - 1) * b^k - (n - 1)) / (k * b^{k - 1} - n)
    """
    n = int(n)
    kmax = round(math.log(n + 1, 2))
    if 2 ** kmax == n:
      return "2"
    f = lambda b, k: ((k - 1) * (b ** k) - (n - 1)) / (k * b ** (k - 1) - n)
    for k in range(kmax, 2, -1):
      bprev = math.exp(math.log(n) / (k - 1))
      bnext = f(bprev, k)
      while not round(bnext) == round(bprev):
        bprev = bnext
        bnext = f(bprev, k)
      binit = round(bnext)
      if binit > 1 and (binit ** k - 1) // (binit - 1) == n:
        return str(binit)
    return str(n - 1)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    # "3",
    # "13",
    "15",
    # "3541",
    # "4681",
    # "14500751095055161",
    # "1000000000000000000",
  ]
  rslts = [solver.smallestGoodBase(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")