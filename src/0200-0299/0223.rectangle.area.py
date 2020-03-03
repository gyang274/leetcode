class Solution:
  def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
    ABCD = (C - A) * (D - B)
    EFGH = (G - E) * (H - F)
    # no overlap if no x-overlap or no y-overlap
    if (A >= G or C <= E) or (B >= H or D <= F):
      return ABCD + EFGH
    else:
      I = max(A, E)
      J = max(B, F)
      K = min(C, G)
      H = min(D, H)
      IJKH = (K - I) * (H - J)
      return ABCD + EFGH - IJKH

class Solution:
  def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
    ABCD = (C - A) * (D - B)
    EFGH = (G - E) * (H - F)
    # no overlap if no x-overlap or no y-overlap
    IJKH = 0
    if not ((A >= G or C <= E) or (B >= H or D <= F)):
      I = max(A, E)
      J = max(B, F)
      K = min(C, G)
      H = min(D, H)
      IJKH = (K - I) * (H - J)
    return ABCD + EFGH - IJKH

class Solution:
  def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
    return (A-C)*(B-D) + (E-G)*(F-H) - max(min(C,G)-max(A,E), 0)*max(min(D,H)-max(B,F), 0)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (-3, 0, 3, 4, 0, -1, 9, 2),
  ]
  rslts = [solver.computeArea(*nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")