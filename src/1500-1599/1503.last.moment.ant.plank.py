from typing import List

class Solution:
  def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
    # if an ant stay on x and move right, no matter how, some ant is keep moving right until reach to n,
    # so the total time to fall is (n - x), similarly, if stay on x and move left the total time is x - 0
    return max(n - min(right or [float('inf')]), max(left or [float('-inf')]))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (4, [4,3], [0,1]),
    (7, [4,2], [3,5]),
    (7, [], [0,1,2,3,4,5,6,7]),
    (7, [0,1,2,3,4,5,6,7], []),
  ]
  rslts = [solver.getLastMoment(n, left, right) for n, left, right in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
