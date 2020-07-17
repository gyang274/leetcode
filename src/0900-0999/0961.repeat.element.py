from typing import List

class Solution:
  def repeatedNTimes(self, A: List[int]) -> int:
    """TC: O(N), SC: O(N), hash.
    """
    d = {}
    for x in A:
      if x in d:
        return x
      d[x] = 1
    return -1

class Solution:
  def repeatedNTimes(self, A: List[int]) -> int:
    """TC: O(N), SC: O(1), pigeonhole principle.
    """
    n = len(A)
    for i in range(n):
      for k in range(1, 4):
        if i + k < n and A[i] == A[i + k]:
          return A[i]
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,1,1,4],
  ]
  rslts = [solver.repeatedNTimes(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
