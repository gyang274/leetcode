import math

class Solution:
  def countOrders(self, n: int) -> int:
    return (math.factorial(2 * n) // (2 ** n)) % (10 ** 9 + 7)

class Solution:
  def countOrders(self, n: int) -> int:
    return (math.factorial(n * 2) >> n) % (10 ** 9 + 7)

class Solution:
  def countOrders(self, n: int) -> int:
    ans, M = 1, 10 ** 9 + 7
    for i in range(2, n + 1):
      ans = (ans * (i * 2 - 1) * (i * 2) // 2) % M
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2, 3, 5, 8, 23, 42, 85,
  ]
  rslts = [solver.countOrders(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
