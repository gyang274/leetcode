from typing import List

class Solution:
  def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
    return list(range(rounds[0], rounds[-1] + 1)) or list(range(1, rounds[-1] + 1)) + list(range(rounds[0], n + 1))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (4, [1,3,1,2]),
    (7, [1,3,5,7]),
    (2, [2,1,2,1,2]),
  ]
  rslts = [solver.mostVisited(n, rounds) for n, rounds in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
