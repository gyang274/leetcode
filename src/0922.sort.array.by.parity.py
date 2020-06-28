from typing import List

class Solution:
  def sortArrayByParityII(self, A: List[int]) -> List[int]:
    """O(N), in-place.
    """
    s0, s1, n = [], [], len(A)
    for i in range(n):
      if (i & 1) ^ (A[i] & 1):
        if i & 1:
          if s0:
            j = s0.pop()
            A[i], A[j] = A[j], A[i]
          else:
            s1.append(i)
        else:
          if s1:
            j = s1.pop()
            A[i], A[j] = A[j], A[i]
          else:
            s0.append(i)
    return A

class Solution:
  def sortArrayByParityII(self, A: List[int]) -> List[int]:
    """O(N), in-place.
    """
    j = 1
    for i in range(0, len(A), 2):
      if A[i] % 2:
        while A[j] % 2:
          j += 2
        A[i], A[j] = A[j], A[i]
    return A

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [4,2,3,1],
  ]
  rslts = [solver.sortArrayByParityII(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
