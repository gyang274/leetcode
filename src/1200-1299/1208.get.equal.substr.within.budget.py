from collections import deque

class Solution:
  def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
    # maintain a queue of (init-index, cost to make equal from init index to this one)
    queue, m = deque([[-1, 0]]), 0
    for i, (x, y) in enumerate(zip(s, t)):
      k = abs(ord(x) - ord(y))
      if k:
        while queue and queue[0][1] + k > maxCost:
          queue.popleft()
        for j in range(len(queue)):
          queue[j][1] += k
      if queue:
        m = max(m, i - queue[0][0])
      queue.append([i, 0])
    return m

class Solution:
  def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
    costs = [abs(ord(x) - ord(y)) for x, y in zip(s, t)]
    i, j, k, m = 0, 0, 0, 0
    while j < len(costs):
      while j < len(costs) and k <= maxCost:
        k += costs[j]
        j += 1
      m = max(m, j - i - 1)
      while i < len(costs) and k > maxCost:
        k -= costs[i]
        i += 1
    m = max(m, j - i)
    return m

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("abcd", "abcd", 3),
    ("abcd", "bcdf", 3),
    ("abcd", "cdef", 3),
    ("abcd", "acde", 0),
    ("krrgw", "zjxss", 19),
  ]
  rslts = [solver.equalSubstring(s, t, maxCost) for s, t, maxCost in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
