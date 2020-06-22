class Solution:
  def consecutiveNumbersSum(self, N: int) -> int:
    """TC: O(sqrt(N)), SC: O(1).
    """
    i, count = 0, 0
    while N > i:
      N -= i
      if N % (i + 1) == 0:
        count += 1
      i += 1
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2, 3, 5, 8, 9, 15, 23, 42, 85,
  ]
  rslts = [solver.consecutiveNumbersSum(N) for N in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
