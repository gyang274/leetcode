class Solution:
  def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    n, m, x, count = numBottles, 0, numExchange, 0
    while n:
      count += n
      n, m = (m + n) // x, (m + n) % x
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, 3), (3, 2), (8, 5), (9, 3), (15, 4),
  ]
  rslts = [solver.numWaterBottles(numBottles, numExchange) for numBottles, numExchange in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
