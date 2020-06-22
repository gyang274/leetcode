from typing import List
from collections import deque

class Solution:
  def sortArrayByParity(self, A: List[int]) -> List[int]:
    ans = deque([])
    for x in A:
      if x & 1:
        ans.append(x)
      else:
        ans.appendleft(x)
    return ans

class Solution:
  def sortArrayByParity(self, A: List[int]) -> List[int]:
    """O(N), in-place.
    """
    i, j = 0, len(A) - 1
    while i < j:
      while i < j and A[i] & 1 == 0:
        i += 1
      while i < j and A[j] & 1 == 1:
        j -= 1
      if i < j:
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1
    return A

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
  ]
  rslts = [solver.sortArrayByParity(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
