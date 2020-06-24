class Solution:
  def smallestRangeII(self, A: List[int], K: int) -> int:
    # A sort, let say A[i] s.t., A[j] + K for j <= i, and A[j] - K for j > i.
    A.sort()
    ans = A[-1] - A[0]
    for i in range(len(A) - 1):
      ans = min(ans, max(A[-1] - K, A[i] + K) - min(A[0] + K, A[i + 1] - K))
    return ans