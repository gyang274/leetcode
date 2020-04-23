from typing import List

class Solution:
  def findLongestChain(self, pairs: List[List[int]]) -> int:
    pairs.sort(key=lambda x: (x[1], x[0]))
    e, count = pairs[0][0] - 1, 0
    for pair in pairs:
      if pair[0] > e:
        e = pair[1]
        count += 1
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,2], [2,3], [3,4]],
  ]
  rslts = [solver.findLongestChain(pairs) for pairs in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
