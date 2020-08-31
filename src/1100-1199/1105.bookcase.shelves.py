from typing import List

class Solution:
  def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
    n = len(books)
    # dp[j]: min heigh upto j-th book
    # dp[j] = min(dp[i - 1] + max(books[i][1])), all js <= i on one shelf
    dp = [float('inf')] * (n + 1)
    # dp[0]: no book
    dp[0] = 0
    # dp[i + 1]: place i-th book on shelf
    for j in range(n):
      w, h = 0, 0
      for i in range(j, -1, -1):
        w += books[i][0]
        if w > shelf_width:
          break
        h = max(h, books[i][1])
        dp[j + 1] = min(dp[j + 1], dp[i] + h)
    return dp[n]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4),
  ]
  rslts = [solver.minHeightShelves(books, shelf_width) for books, shelf_width in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
