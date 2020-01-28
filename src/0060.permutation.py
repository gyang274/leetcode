import math


class Solution:
  def getPermutation(self, n: int, k: int) -> str:
    s = ""
    x = [i for i in range(1, n + 1)]
    z = math.factorial(n - 1)
    for i in range(n):
      j = (k - 1) // z
      s += str(x[j])
      x.remove(x[j])
      k %= z
      z //= max(1, (n - 1 - i))
    return s

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    (3, 3),
    (4, 9),
  ]
  rslts = [solver.getPermutation(n, k) for n, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}") 