from typing import List

class Solution:
  def splitArraySameAverage(self, A: List[int]) -> bool:
    # if split to B, C with mean(B) == mean(C) then mean(B) == mean(C) == mean(A)
    n = len(A)
    if n < 2:
      return False
    # transform A so that mean(A) == 0 and deals with integer only in the process
    A = [x * n - sum(A) for x in A]
    # zero subset sum w.r.t 2^(N/2) instead of 2^N
    l = {A[0]}
    for i in range(1, n // 2):
      l |= {A[i]} | {s + A[i] for s in l} 
    if 0 in l:
      return True
    r = {A[-1]}
    for i in range(n // 2, n - 1):
      r |= {A[i]} | {s + A[i] for s in r}
    if 0 in r:
      return True
    ll, rr = sum(A[:(n//2)]), sum(A[(n//2):])
    return any(-x in r and not (x, -x) == (ll, rr) for x in l)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,2,3],
    [1,6,1],
    [1,2,3,4,5,6,7,8],
  ]
  rslts = [solver.splitArraySameAverage(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
