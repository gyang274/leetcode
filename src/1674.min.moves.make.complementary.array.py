from typing import List
from collections import Counter

class Solution:
  def minMoves(self, nums: List[int], limit: int) -> int:
    # TC: O(N + L), SC: O(L)
    # To make the nums complementary, consider the pair A = nums[i], B = nums[n - 1 - i] for all T, 2 <= T <= 2 * limit,
    # it reduces to 5 different situations:
    #  1. 2 <= T < min(A, B) + 1, we need 2 operations to make both A, B smaller
    #  2. min(A, B) + 1 <= T < A + B, we need 1 operation to make the larger one out of A and B smaller
    #  3. T = A + B, we need 0 operation
    #  4. A + B < T < max(A, B) + limit, we need 1 operation to make the smaller one out of A and B larger
    #  5. max(A, B) + limit < T <= 2 * limit, we need 2 operation to make both A, B larger
    # So, we can calculate the boundary for each pair (A, B) and note down the corresponding operation changes as delta.
    #  delta[i] = x means we need x more operations when target T change from i - 1 to i.
    n, d, L = len(nums), Counter(), limit
    for i in range(n // 2):
      a, b = nums[i], nums[n - 1 - i]
      d[2] += 2
      d[min(a, b) + 1] -= 1
      d[a + b] -= 1
      d[a + b + 1] += 1
      d[max(a, b) + L + 1] += 1
    x, m = 0, float('inf')
    for i in range(2, 2 * L + 1):
      x += d[i]
      m = min(m, x)
    return m
