from typing import List

class Solution:
  def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    stack = []
    for x in asteroids:
      if x > 0:
        stack.append(x)
      else:
        # x < 0
        while stack and stack[-1] > 0 and stack[-1] + x < 0:
          stack.pop()
        if stack and stack[-1] + x > 0:
          continue
        elif stack and stack[-1] + x == 0:
          stack.pop()
        else:
          stack.append(x)
    return stack

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1, -1],
    [5, 10, -5],
    [10, 2, -5],
    [-2, -1, 1, 2],
  ]
  rslts = [solver.asteroidCollision(asteroids) for asteroids in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
