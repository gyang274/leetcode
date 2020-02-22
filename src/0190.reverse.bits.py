class Solution:
  def reverseBits(self, n: int) -> int:
    ans = 0
    for _ in range(32):
      ans = (ans << 1) + (n & 1)
      n >>= 1
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    0,
    1,
    43261596,
    2147483648,
    4294967293,
  ]
  rslts = [solver.reverseBits(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")