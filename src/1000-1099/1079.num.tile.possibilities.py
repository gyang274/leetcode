from collections import Counter

class Solution:
  def recursive(self, candidate: str):
    for x in self.d:
      if self.d[x] > 0:
        self.d[x] -= 1
        self.ans.add(candidate + x)
        self.recursive(candidate + x)
        self.d[x] += 1
  def numTilePossibilities(self, tiles: str) -> int:
    self.d, self.ans = Counter(tiles), {''}
    self.recursive('')
    return len(self.ans) - 1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "AAB",
    "AAABBC",
  ]
  rslts = [solver.numTilePossibilities(tiles) for tiles in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
