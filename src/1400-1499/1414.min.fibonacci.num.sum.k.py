import bisect

class Solution:
  def __init__(self):
    self.F = [1, 1]
    while self.F[-1] <= 10 ** 9:
      self.F.append(self.F[-2] + self.F[-1])
  def findMinFibonacciNumbers(self, k: int) -> int:
    # greedy
    # greedy works:
    #  1. f(k-1) + f(k) = f(k+1), so no consecutive in optimal solution
    #  2. f(k) * 2 = f(k-2) + f(k+1), so can be no duplicate in optimal solution
    #  3. f(2n+1) = f(2n) + f(2n-1) = f(2n) + f(2n-2) + f(2n-3) = f(2n) + f(2n-2) + .. + f(2) + f(0)
    #     f(2n) = f(2n-1) + f(2n-2) = f(2n-1) + f(2n-3) + f(2n-4) = f(2n-1) + f(2n-3) + .. + f(1) + f(0)
    #     so, no duplicate and no adjacent implies can always take the largest, because, if x >= fibo(2n), 
    #     and don't take fibo(2n), the rest sum of every two F numbers can only reach a maximum fibo(2n) - 1
    count = 0
    while k:
      k -= self.F[bisect.bisect(self.F, k) - 1]
      count += 1
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2, 7, 10, 19, 42, 85,
  ]
  rslts = [solver.findMinFibonacciNumbers(k) for k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
