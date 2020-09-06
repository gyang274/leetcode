class Solution:
  def nthPersonGetsNthSeat(self, n: int) -> float:
    # f(n) = 1 / n + (n - 2) / n * f(n - 1)
    return 1.0 if n == 1 else 0.5