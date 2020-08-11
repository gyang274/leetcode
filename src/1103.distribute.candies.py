from typing import List

class Solution:
  def distributeCandies(self, candies: int, num_people: int) -> List[int]:
    # math
    x, n = candies, num_people
    # m: the last one
    m = round((2 * x) ** 0.5)
    while m * (m + 1) // 2 > x:
      m -= 1
    p, q, r = m // n, m % n, x - m * (m + 1) // 2
    # allocate candies
    ans = [0] * n
    for i in range(0, q):
      ans[i] = (i + 1) * (p + 1) + p * (p + 1) * n // 2
    for i in range(q, n):
      ans[i] = (i + 1) * (p + 0) + (p - 1) * p * n // 2
    ans[q] += r
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (7, 4), (8, 5), (10, 3), (2714, 11),
  ]
  rslts = [solver.distributeCandies(candies, num_people) for candies, num_people in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
