from typing import List

import heapq

class Solution:
  def dailyTemperatures(self, T: List[int]) -> List[int]:
    queue, waits = [], [0] * len(T)
    for i, t in enumerate(T):
      while queue and queue[0][0] < t:
        _, j = heapq.heappop(queue)
        waits[j] = i - j
      heapq.heappush(queue, (t, i))
    return waits

class Solution:
  def dailyTemperatures(self, T: List[int]) -> List[int]:
    stack, waits = [], [0] * len(T)
    for i, t in reversed(list(enumerate(T))):
      while stack and stack[-1][0] <= t:
        stack.pop()
      if stack:
        waits[i] = stack[-1][1] - i
      stack.append((t, i))
    return waits

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [73,73,75,71,69,72,76,73],
  ]
  rslts = [solver.dailyTemperatures(T) for T in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
