class Solution:
  def arrangeCoins(self, n: int) -> int:
    """1 + 2 + .. + k = k * (k + 1) / 2 <= n
      k ~= sqrt(2n + 1/4) - 1
    """
    k = int((2 * n) ** 0.5 + 0.25) - 1
    while k * (k + 1) // 2 <= n:
      k += 1
    return k - 1
    
if __name__ == '__main__':
  solver = Solution()
  cases = [
    2, 3, 5, 8, 42, 714285,
  ]
  rslts = [solver.arrangeCoins(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")