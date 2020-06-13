from typing import List

class Solution:
  def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
    # go through zip(As = sorted(A), Bs = sorted((x, i) for i, x in enumerate(B))
    # Xs[i] = As[j++] if As[j] > x else As[k--] for x, i in Bs, init j, k = 0, n - 1
    N = len(A)
    As, Bs = sorted(A, reverse=True), sorted(((x, i) for i, x in enumerate(B)), reverse=True)
    j, k, Xs = 0, N - 1, [None] * N
    for x, i in Bs:
      if As[j] > x:
        Xs[i] = As[j]
        j += 1
      else:
        Xs[i] = As[k]
        k -= 1
    return Xs

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,3,1,1,4], [3,2,1,0,4]),
  ]
  rslts = [solver.advantageCount(A, B) for A, B in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
