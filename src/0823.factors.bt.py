from typing import List

class Solution:
  def numFactoredBinaryTrees(self, A: List[int]) -> int:
    A.sort()
    d, M = {}, 10 ** 9 + 7
    for x in A:
      d[x] = 1
      for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
          j = x // i
          if i in d and j in d:
            if i == j:
              d[x] += d[i] * d[j]
            else:
              d[x] += d[i] * d[j] * 2
      d[x] %= M
    return sum(d.values()) % M

class Solution:
  def numFactoredBinaryTrees(self, A: List[int]) -> int:
    A.sort()
    d, M = {}, 10 ** 9 + 7
    for i, x in enumerate(A):
      d[x] = 1
      for j in range(i):
        if x % A[j] == 0:
          y, z = A[j], x // A[j]
          if z in d:
            d[x] += d[y] * d[z]
      d[x] %= M
    return sum(d.values()) % M

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,4],
    [2,4,8],
    [2,4,5,10],
    [2,4,8,16],
    [2,4,8,16,32],
  ]
  rslts = [solver.numFactoredBinaryTrees(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
