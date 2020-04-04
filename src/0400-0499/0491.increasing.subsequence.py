from typing import List

class Solution:
  def findSubsequences(self, nums: List[int]) -> List[List[int]]:
    ans = [[]]
    for x in nums:
      candidates = []
      for seq in ans:
        if (not seq or x >= seq[-1]) and (seq + [x] not in ans):
          candidates.append(seq + [x])
      ans.extend(candidates)
    return [seq for seq in ans if len(seq) > 1]

class Solution:
  def findSubsequences(self, nums: List[int]) -> List[List[int]]:
    ans = {()}
    for x in nums:
      ans |= {seq + (x, ) for seq in ans if not seq or x >= seq[-1]}
    return [list(seq) for seq in ans if len(seq) >= 2]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [1],
    [1,2,3],
    [2,3,1,1,4],
    [4,6,7,7,8],
  ]
  rslts = [solver.findSubsequences(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  