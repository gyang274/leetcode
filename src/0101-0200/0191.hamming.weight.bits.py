class Solution:
  def hammingWeight(self, n: int) -> int:
    """bit manipulation:
      n & (n - 1) flip the rightmost 1 into 0
      n & ~(n - 1) get out rigthmost 1 with trailing zeros, e.g., rightmost 1's index
    """
    ans = 0
    while n > 0:
      n &= (n - 1)
      ans += 1
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    0,
    1,
    2,
    3,
    43261596,
    2147483648,
    4294967293,
  ]
  rslts = [solver.hammingWeight(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")