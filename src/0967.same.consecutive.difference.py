from typing import List

class Solution:
  def recursive(self, x, i):
    if i == self.N:
      self.ans.append(x)
    elif i == 0:
      for d in range(1, 10):
        self.recursive(d, 1)
    else:
      d = x % 10
      if d - self.K >= 0:
        self.recursive(x * 10 + (d - self.K), i + 1)
      if d + self.K <= 9:
        self.recursive(x * 10 + (d + self.K), i + 1)
  def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
    if N == 1:
      return [0,1,2,3,4,5,6,7,8,9]
    if K == 0:
      return [int(str(i) * N) for i in range(1, 10)]
    self.ans, self.N, self.K = [], N, K
    self.recursive(None, 0)
    return self.ans

class Solution:
  def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
    ans = {x for x in range(1, 10)}
    for _ in range(N-1):
      ant = set()
      for x in ans:
        d = x % 10
        if d - K >= 0:
          ant.add(x * 10 + (d - K))
        if d + K <= 9:
          ant.add(x * 10 + (d + K))
      ans = ant
    if N == 1:
      ans.add(0)
    return list(ans)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, 3),
    (3, 5),
    (5, 8),
  ]
  rslts = [solver.numsSameConsecDiff(N, K) for N, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
