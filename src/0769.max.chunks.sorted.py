from typing import List

class Solution:
  def maxChunksToSorted(self, arr: List[int]) -> int:
    """O(N), one pass.
    """
    smax, chunks = -1, 0
    for i, x in enumerate(arr):
      smax = max(smax, x)
      if smax == i:
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
