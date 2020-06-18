class Solution:
  def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
    d, B = (sum(A) - sum(B)) // 2, set(B)
    for x in A:
      if x - d in B:
        return [x, x - d]
        