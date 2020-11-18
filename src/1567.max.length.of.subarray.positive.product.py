from typing import List

class Solution:
  def getMaxLen(self, nums: List[int]) -> int:
    # cneg: count of negative, after last zero
    # ineg: index of 1st negative, after last zero
    # clen: length of subarray, after last zero
    # cmax: max length of subarray with positive product
    cneg, ineg, clen, cmax = 0, -1, 0, 0
    for i, x in enumerate(nums):
      if x == 0:
        cneg, ineg, clen = 0, -1, 0
      elif x < 0:
        cneg += 1
        if ineg < 0:
          ineg = i
        clen += 1
      else:
        clen += 1
      if (cneg & 1) ^ 1:
        cmax = max(cmax, clen)
      else:
        cmax = max(cmax, i - ineg)
    return cmax

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [0,1,-2,-3,-4],
  ]
  rslts = [solver.getMaxLen(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
