from typing import List

class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    ss = set()
    for i, s in enumerate(nums[:-2]):
      if s not in ss:
        ss.add(s)
        xs = set()
        ys = set()
        for j, x in enumerate(nums[(i+1):]):
          if x not in xs:
            if -(s + x) not in ys:
              ys.add(x)
            else:
              res.append([s, -(s + x), x])
              xs.add(x)
    return res

if __name__ == '__main__':
  solver = Solution()
  numsList = [
    [-1, 0, 1, 2, -1, -4],
    [0, 0, 0, 0],
  ]
  soluList = [solver.threeSum(nums) for nums in numsList]
  for xn, xs in zip(numsList, soluList):
    print(f"nums: {xn} | solution: {xs}")
