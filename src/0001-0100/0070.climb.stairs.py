import math


class Solution:
  def climbStairs(self, n: int) -> int:
    """Dynamic programming, Fibonacci sequence.
    """
    memo = [0 for _ in range(n + 2)]
    memo[0] = 1
    memo[1] = 1
    for i in range(2, n + 1):
      memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]

class Solution:
  def climbStairs(self, n: int) -> int:
    """Dynamic programming, Fibonacci sequence.
    """
    return int((((1 + math.sqrt(5)) / 2) ** (n + 1) - ((1 - math.sqrt(5)) / 2) ** (n + 1)) / math.sqrt(5))


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    0,
    1,
    2,
    3,
    4,
    5,
  ]
  rslts = [solver.climbStairs(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")