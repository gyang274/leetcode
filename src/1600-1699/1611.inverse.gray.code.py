class Solution:
  dp = {0: 0}
  def minimumOneBitOperations(self, n: int) -> int:
    # Observation 1
    #  The two operations are undo-able/reversible.
    #  If x -> y needs k operation, y -> x also needs k operation.
    # Observation 2
    #  1 -> 0 needs 1 operation,
    #  2 -> 0 needs 3 operations,
    #  4 -> 0 needs 7 operations,
    #  2^k needs 2^(k+1)-1 operations.
    # Operations path:
    #  1XXX -> 1100 -> 100 -> 0
    # Operations path with counts:
    #  1XXX -> 1100 needs minimumOneBitOperations(1XXX ^ 1100), 
    #  this is because it needs same operations 1XXX ^ 1100 -> 1100 ^ 1100 = 0.
    # In summary,
    #  1100 -> 100 needs 1 operation, and 100 -> 0 needs 2^(k-1) - 1 operations, since 100 is 2^k.
    if n not in self.dp:
      b = 1
      while (b << 1) <= n:
        b <<= 1
      self.dp[n] = self.minimumOneBitOperations(n ^ (b ^ (b >> 1))) + 1 + (b - 1)
    return self.dp[n]

class Solution:
  def minimumOneBitOperations(self, n: int) -> int:
    # inverse gray code, e.g., the rank/position along gray code..
    x = 0
    while n:
      x ^= n
      n >>= 1
    return x

if __name__ == '__main__':
  solver = Solution()
  cases = [
    0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8,
  ]
  rslts = [solver.minimumOneBitOperations(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
