from collections import defaultdict

class Solution:
  def sumOfDigits(self, x):
    s = 0
    while x:
      s += x % 10
      x //= 10
    return s
  def countLargestGroup(self, n: int) -> int:
    d = defaultdict(lambda: 0)
    for x in range(1, n + 1):
      d[self.sumOfDigits(x)] += 1
    m = max(d.values())
    return len([s for s in d if d[s] == m])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2, 3, 5, 8, 23, 42, 85,
  ]
  rslts = [solver.countLargestGroup(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
