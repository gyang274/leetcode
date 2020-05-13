from typing import List

class Solution:
  def maxChunksToSorted(self, arr: List[int]) -> int:
    """O(N), 3 pass.
    """
    n = len(arr)
    # smax: max from left
    # smin: min from right
    smax, smin = arr.copy(), arr.copy()
    for i in range(1, n):
      smax[i] = max(smax[i - 1], smax[i])
    for i in range(n - 2, -1, -1):
      smin[i] = min(smin[i], smin[i + 1])
    # at any i, if smin[i] >= smax[i - 1] then a split can be made between i - 1 and i
    chunks = 1
    for i in range(1, n):
      if smin[i] >= smax[i - 1]:
        chunks += 1
    return chunks

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,0,4,2,3],
    [2,3,1,0,4],
    [4,3,2,1,0],
  ]
  rslts = [solver.maxChunksToSorted(arr) for arr in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
