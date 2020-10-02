from typing import List

class Solution:
  def numOfOneBits(self, x):
    n = 0
    while x:
      n += x & 1
      x >>= 1
    return n
  def sortByBits(self, arr: List[int]) -> List[int]:
    arr.sort(key=lambda x: (self.numOfOneBits(x), x))
    return arr

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
  ]
  rslts = [solver.sortByBits(arr) for arr in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
