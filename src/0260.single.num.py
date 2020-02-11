from typing import List

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    """Binary xor `^` operator, if x ^ y = z, then x ^ z = y.
    """
    # suppose the singltons are a and b, x = a ^ b
    x = 0
    for y in nums:
      x ^= y
    # x & (-x) gives x's rightmost 1-bit position, 
    # so this is the position a has 1 and b has 0 or vice versa
    z = x & (-x)
    # thus, z & a = 1 and z & b = 0 or vice versa
    a = 0
    for y in nums:
      if z & y:
        a ^= y
    return [a, x ^ a]

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [0,1],
    [2,2,3,5],
    [0,1,0,1,2,3]
  ]
  rslts = [solver.singleNumber(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  