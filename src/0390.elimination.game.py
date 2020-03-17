class Solution:
  def lastRemaining(self, n: int) -> int:
    # f(n) = 2 * (1 + n//2 - f(n//2))
    return 1 if n == 1 else 2 * (1 + n // 2 - self.lastRemaining(n // 2))

class Solution:
  def lastRemaining(self, n: int) -> int:
    # Josephus problem
    # i: i-th round, lr: left to right 0 or right to left 1, rr: 1st after i-th round result
    i, lr, rr = 0, 0, 0
    while n > 1:
      mask = 1 << i
      # left to right: equivalent as set i-th rightmost bit to 0
      # right to left: equivalent as xor i-th rightmost bit, e.g., 0 -> 1, 1 -> 0
      b = (((n & 1) ^ 1) & lr) ^ (rr > 0)
      # set rr's binary i-th position to b
      rr = (rr & ~mask) | ((b << i) & mask)
      # next
      n >>= 1
      lr ^= 1
      i += 1
    if rr == 0:
      rr = 1 << i
    return rr

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2, 3, 5, 8, 42, 85,
  ]
  rslts = [solver.lastRemaining(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
