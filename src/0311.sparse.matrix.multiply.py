from typing import List
from collections import defaultdict

class Solution:
  def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """C=AB, C_{ij} = sum_k A_{ik} * B_{kj}, so only if not A_{ik} * B_{kj} == 0 for some k.
    """
    # A's non-zero i -> all k
    nzik = defaultdict(set)
    for i in range(len(A)):
      for k in range(len(A[i])):
        if A[i][k]:
          nzik[i].add(k)
    # B's non-zero k -> all j
    nzkj = defaultdict(set)
    for k in range(len(B)):
      for j in range(len(B[k])):
        if B[k][j]:
          nzkj[k].add(j)
    # C
    C = [[0] * len(B[0]) for _ in range(len(A))]
    for i in nzik:
      for k in nzik[i]:
        for j in nzkj[k]:
          C[i][j] += A[i][k] * B[k][j]
    return C

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (
      [
        [ 1, 0, 0],
        [-1, 0, 3]
      ],
      [
        [ 7, 0, 0 ],
        [ 0, 0, 0 ],
        [ 0, 0, 1 ]
      ]
    ),
  ]
  rslts = [solver.multiply(A, B) for A, B in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")