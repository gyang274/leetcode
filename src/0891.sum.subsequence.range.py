class Solution:
  def sumSubseqWidths(self, A: List[int]) -> int:
    # A sorted: [A0, A1, .., A(n-1)]
    # Ai is the maximum of 2^i subsequences, is the minimum of 2^(n - 1 - i) subsequences
    A.sort()
    return sum(((x << i) - (x << (len(A) - 1 - i))) for i, x in enumerate(A)) % (10 ** 9 + 7)
