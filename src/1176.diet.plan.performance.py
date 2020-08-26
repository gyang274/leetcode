from typing import List

class Solution:
  def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
    count = 0
    # init, day [0, k)
    s = sum(calories[:k])
    count += -1 * (s < lower) + 1 * (s > upper)
    for i in range(k, len(calories)):
      s += calories[i] - calories[i - k]
      count += -1 * (s < lower) + 1 * (s > upper)
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([3,2], 2, 0, 1),
    ([1,2,3,4,5], 1, 3, 3),
  ]
  rslts = [solver.dietPlanPerformance(calories, k, lower, upper) for calories, k, lower, upper in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
