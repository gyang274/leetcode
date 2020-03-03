class Solution:
  def isUgly(self, num: int) -> bool:
    """bit manipulation:
      n & (n - 1) flip the rightmost 1 into 0
      n & ~(n - 1) or n & (-n) get out rigthmost 1 with trailing zeros, e.g., rightmost 1's index
    """
    if num > 0:
      # num % 2 == 0 -> num //= 2
      while num & (-num) > 1:
        num >>= 1
      # num % 3 == 0 -> num //= 3
      while num % 3 == 0:
        num //= 3
      # num % 5 == 0 -> num //= 5
      while num % 5 == 0:
        num //= 5
      if num == 1:
        return True
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    -10, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 42, 85,
  ]
  rslts = [solver.isUgly(num) for num in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
