from typing import List

class Solution:
  def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
    n = len(heights)
    for _ in range(V):
      stack = [heights[K]]
      # left
      i = K - 1
      while i > -1 and heights[i] <= stack[-1]:
        stack.append(heights[i])
        i -= 1
      while len(stack) > 1 and stack[-2] == stack[-1]:
        stack.pop()
      if len(stack) > 1:
        heights[K - len(stack) + 1] += 1
        continue
      # right
      i = K + 1
      while i < n and heights[i] <= stack[-1]:
        stack.append(heights[i])
        i += 1
      while len(stack) > 1 and stack[-2] == stack[-1]:
        stack.pop()
      if len(stack) > 1:
        heights[K + len(stack) - 1] += 1
        continue
      heights[K] += 1
    return heights

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,3,1,1,4], 2, 3),
    ([2,1,1,2,1,2,2], 4, 3),
  ]
  rslts = [solver.pourWater(heights, V, K) for heights, V, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
