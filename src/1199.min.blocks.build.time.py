from typing import List

class Solution:
  def recursive(self, num_worker, blocks):
    if (num_worker, blocks) not in self.memo:
      if num_worker >= len(blocks):
        self.memo[(num_worker, blocks)] = blocks[0]
      else:
        # default, all split
        self.memo[(num_worker, blocks)] = self.split + self.recursive(num_worker * 2, blocks)
        # some split, some build, mitigate empty list in max()
        for x in range(1, num_worker):
          self.memo[(num_worker, blocks)] = min(self.memo[(num_worker, blocks)], 
            max(self.split + self.recursive((num_worker - x) * 2, blocks[x:]), *blocks[:x])
          )
    return self.memo[(num_worker, blocks)]
  def minBuildTime(self, blocks: List[int], split: int) -> int:
    blocks = tuple(sorted(blocks, reverse=True))
    self.memo, self.split = {}, split
    return self.recursive(1, blocks)

import heapq

class Solution:
  def minBuildTime(self, blocks: List[int], split: int) -> int:
    # Huffman's algorithm, TC: O(NlogN), SC: O(N).
    heapq.heapify(blocks)
    while len(blocks) > 1:
      x, y = heapq.heappop(blocks), heapq.heappop(blocks)
      heapq.heappush(blocks, y + split)
    return heapq.heappop(blocks)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1], 1),
    ([1,2], 5),
    ([1,2,3], 1),
  ]
  rslts = [solver.minBuildTime(blocks, split) for blocks, split in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
