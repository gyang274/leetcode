from typing import List

class Solution:
  def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
    ans, s = [], sum(filter(lambda x: (x & 1) ^ 1, A))
    for x, i in queries:
      if A[i] & 1:
        if x & 1:
          s += A[i] + x
      else:
        if x & 1:
          s -= A[i]
        else:
          s += x
      ans.append(s)
      A[i] += x
    return ans

class Solution:
  def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
    ans, s = [], sum(filter(lambda x: (x & 1) ^ 1, A))
    for x, i in queries:
      if (A[i] & 1) ^ 1:
        s -= A[i]
      A[i] += x
      if (A[i] & 1) ^ 1:
        s += A[i]
      ans.append(s)
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]),
  ]
  rslts = [solver.sumEvenAfterQueries(A, queries) for A, queries in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
