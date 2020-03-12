from typing import List

class Solution:
  def _search(self, array: List[int], target: int) -> int:
    """modified binary search find largest x <= target in sorted array.
    """
    l, r = 0, len(array)
    while l < r:
      m = l + (r - l) // 2
      # if array[m] == target:
      #   return array[m]
      if array[m] >= target:
        r = m
      else:
        l = m + 1
    return l
  def maxSumSubarray(self, array: List[int], k: int) -> int:
    xmax, stack = float('-inf'), []
    for i in range(len(array)):
      if array[i] <= k:
        xmax = max(xmax, array[i])
      # update xmax if any j < i, s.t. array[i] - array[j] <= k, e.g., array[j] >= array[i] - k
      j = self._search(stack, array[i] - k)
      if j < len(stack):
        xmax = max(xmax, array[i] - stack[j])
      # insert array i-th item into stack
      j = self._search(stack, array[i])
      stack.insert(j, array[i])
    return xmax
  def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
    """Q0304 + modified binary search, O(N^2 * MlogM), N < M.
    """
    # assume n <= m, so linear over n, binary search over m
    n, m = len(matrix), len(matrix[0])
    if n > m:
      # transpose the matrix
      matrix = [[matrix[j][i] for j in range(n)] for i in range(m)]
      n, m = m, n
    # build the partial sum
    for i in range(1, n):
      matrix[i][0] += matrix[i - 1][0]
    for j in range(1, m):
      matrix[0][j] += matrix[0][j - 1]
    for i in range(1, n):
      for j in range(1, m):
        matrix[i][j] += matrix[i][j - 1] + matrix[i - 1][j] - matrix[i - 1][j - 1]
    # assume n <= m, so double loop over n (rows), binary search over m (cols)
    xmax = float('-inf')
    for i1 in range(n):
      r11 = matrix[i1]
      xmax = max(xmax, self.maxSumSubarray(r11, k))
      for i2 in range(i1 + 1, n):
        r12 = [matrix[i2][j] - matrix[i1][j] for j in range(m)]
        xmax = max(xmax, self.maxSumSubarray(r12, k))
    return xmax

# class Solution:
#   def a():
#     """Q0308, segment tree 2d, O(NMlogNlogM).
#     """
#     return x

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[2,2,-1]], 0),
    ([[2,2,-1]], 3),
    ([[1,0,1],[0,-2,3]], 2),
  ]
  rslts = [solver.maxSumSubmatrix(matrix, k) for matrix, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
