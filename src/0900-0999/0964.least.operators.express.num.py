from collections import deque

class Solution:
  def leastOpsExpressTarget(self, x: int, target: int) -> int:
    if x == target:
      return 0
    # maintain a queue of (value-before-last-"+/-", value-after-last-"+/-", num-operator)
    queue, seen = deque([(0, x, 0)]), {(0, x)}
    while queue:
      v0, v1, k =  queue.popleft()
      # add "+"
      if v0 + v1 + x == target:
        return k + 1
      if (v0 + v1, x) not in seen:
        seen.add((v0 + v1, x))
        queue.append((v0 + v1,  x, k + 1))
      # add "-"
      if v0 + v1 - x == target:
        return k + 1
      if (v0 + v1, -x) not in seen:
        seen.add((v0 + v1, -x))
        queue.append((v0 + v1, -x, k + 1))
      # add "x"
      if v0 + v1 * x == target:
        return k + 1
      if (v0, v1 * x) not in seen:
        queue.append((v0, v1 * x, k + 1))
      # add "//"
      if v0 + v1 // x == target:
        return k + 1
      if v1 // x > 0 and (v0, v1 // x) not in seen:
        seen.add((v0, v1 // x))
        queue.append((v0, v1 // x, k + 1))
    return -1

import heapq

class Solution:
  def leastOpsExpressTarget(self, x: int, target: int) -> int:
    items = [(0, x, [x]), (1, 1, [1])]
    seen = {}
    seen[1] = 1
    seen[x] = 0
    v, k = x, 0
    while v < target:
      v *= x
      k += 1
      seen[v] = k
      items.append((k, v, [v]))
    queue = list(items)
    while queue:
      k, v, p = heapq.heappop(queue)
      if v == target:
        return k
      if seen[v] == k:
        for xk, xv, xp in items:
          if v + xv not in seen or seen[v + xv] > k + xk + 1:
            seen[v + xv] = k + xk + 1
            heapq.heappush(queue, (k + xk + 1, v + xv, p + [xv]))
          if v - xv not in seen or seen[v - xv] > k + xk + 1:
            seen[v - xv] = k + xk + 1
            heapq.heappush(queue, (k + xk + 1, v - xv, p + [-xv]))
    return -1

class Solution:
  def leastOpsExpressTarget(self, x: int, target: int) -> int:
    """TC: O(logT). T = target, trace T % (x^k).
    """
    y, x = target, x
    # pos the number of operations needed to get y % (x ^ (k+1))
    # neg the number of operations needed to get x ^ (k + 1) - y % (x ^ (k + 1))
    pos, neg, k = 0, 0, 0
    while y:
      y, cur = divmod(y, x)
      if not k:
        pos, neg = cur * 2, (x - cur) * 2
      else:
        pos, neg = min(cur * k + pos, (cur + 1) * k + neg), min((x - cur) * k + pos, (x - cur - 1) * k + neg)
      k += 1
    return min(pos, k + neg) - 1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, 23),
    (3, 42),
    (5, 85),
    (8, 274),
    (2, 500094),
  ]
  rslts = [solver.leastOpsExpressTarget(x, target) for x, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
