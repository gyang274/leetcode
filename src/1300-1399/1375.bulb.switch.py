from typing import List

class Solution:
  def numTimesAllBlue(self, light: List[int]) -> int:
    # r: rightmost light on bulb, all blue iff r == i + 1
    r, count = 0, 0
    for i, x in enumerate(light):
      r = max(r, x)
      if r == i + 1:
        count += 1
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,4,5],
    [2,1,3,5,4],
  ]
  rslts = [solver.numTimesAllBlue(light) for light in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
