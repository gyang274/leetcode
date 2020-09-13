from functools import lru_cache

class Solution:
  @lru_cache(None)
  def numberOfWays(self, num_people: int) -> int:
    n = num_people
    if n < 3:
      return 1
    count = 0
    for i in range(1, n, 2):
      count += self.numberOfWays(i - 1) * self.numberOfWays(n - 1 - i)
    return count % (10 ** 9 + 7)

class Solution:
  def numberOfWays(self, num_people: int) -> int:
    n = num_people
    # Catalan numbers
    count = 1
    for i in range(1, n // 2 + 1):
      count *= n - i + 1
      count //= i
    return count // (n // 2 + 1) % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2, 4, 6, 8, 10, 22, 42, 714,
  ]
  rslts = [solver.numberOfWays(num_people) for num_people in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
