from typing import List

class Solution:
  def closestDivisors(self, num: int) -> List[int]:
    for i in range(int((num + 2) ** 0.5), 0, -1):
      if (num + 1) % i == 0:
        return (i, (num + 1) // i)
      if (num + 2) % i == 0:
        return (i, (num + 2) // i)
    return None

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2, 3, 5, 8, 23, 42, 85,
  ]
  rslts = [solver.closestDivisors(num) for num in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
