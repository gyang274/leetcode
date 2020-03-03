from typing import List

class Solution:
  def majorityElement(self, nums: List[int]) -> List[int]:
    """annihilation
      1st generate candidates see once +1, see any outside both candidates -1, and if > ceil(n/3) then count > 0, 
      2nd pass to confirm candidates are the majority elements since existence is not given by default.
    """  
    # 1st pass candidate annihilation
    s1, c1, s2, c2 = None, 0, None, 0
    for x in nums:
      if x == s1:
        c1 += 1
      elif x == s2:
        c2 += 1
      elif c1 == 0:
        s1, c1 = x, 1
      elif c2 == 0:
        s2, c2 = x, 1
      else:
        c1 -= 1
        c2 -= 1
    # 2nd pass majority confirmation
    return [x for x in (s1, s2) if nums.count(x) > len(nums) // 3]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [0],
    [0,1],
    [0,0,1],
    [3,2,3],
    [4,2,1,1],
    [0,-1,2,-1],
    [1,1,2,3,3,3],
    [1,1,1,3,3,2,2,2],
  ]
  rslts = [solver.majorityElement(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")