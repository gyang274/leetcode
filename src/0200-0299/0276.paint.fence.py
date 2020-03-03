class Solution:
  def numWays(self, n: int, k: int) -> int:
    """status machine, keep track
      s1 and s2: num of ways last 2 fences same color (.., c_i, c_i) and different color (.., c_i, c_j), respectively.
    """
    if n == 0:
      return 0
    # n == 1
    s1, s2 = 0, k
    for _ in range(2, n + 1):
      s1, s2 = s2, (s1 + s2) * (k - 1)
    return s1 + s2