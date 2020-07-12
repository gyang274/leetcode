from typing import List

import bisect

class Solution:
  def oddEvenJumps(self, A: List[int]) -> int:
    n = len(A)
    if n == 1:
      return 1
    # init
    # d: (value, index) -> [T/F if odds, T/F if even]
    d = {}
    d[(A[-1], n - 1)] = [True, True]
    so, se = [(+A[-1], n - 1)], [(-A[-1], n - 1)]
    # main
    for i in range(n - 2, -1, -1):
      j = bisect.bisect(so, (+A[i], 0))
      odds = d[(+so[j][0], so[j][1])][1] if j < len(so) else False
      k = bisect.bisect(se, (-A[i], 0))
      even = d[(-se[k][0], se[k][1])][0] if k < len(se) else False
      d[(A[i], i)] = (odds, even)
      # print(f"{(A[i], i)=}, {so=}, {j=}, {se=}, {k=}, {d[(A[i], i)]=}")
      bisect.insort(so, (+A[i], i))
      bisect.insort(se, (-A[i], i))
    return sum(d[k][0] for k in d)

class Solution:
  def oddEvenJumps(self, A: List[int]) -> int:
    n = len(A)
    if n == 1:
      return 1
    # init:
    # d: value -> smallest index in A, True/False if odds, True/False if even
    d, s, count = {A[-1]: [1, 1]}, [A[-1]], 1
    # main
    for i in range(n - 2, -1, -1):
      j = bisect.bisect_left(s, A[i])
      if j < len(s) and A[i] == s[j]:
        d[A[i]] = d[s[j]][::-1]
      else:
        d[A[i]] = [0, 0]
        if j < len(s):
          d[A[i]][0] = d[s[j]][1]
        if j > 0:
          d[A[i]][1] = d[s[j - 1]][0]
        bisect.insort(s, A[i])
      count += d[A[i]][0]
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
    [1,2,3,2,1,4,4,5],
  ]
  rslts = [solver.oddEvenJumps(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
