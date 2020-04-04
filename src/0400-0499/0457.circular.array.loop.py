from typing import List

class Solution:
  def circularArrayLoop(self, nums: List[int]) -> bool:
    """TC: O(n), SC: O(1).
    """
    # i: index to start
    i, n = 0, len(nums)
    while i < n:
      # skip if visited or self-loop
      if isinstance(nums[i], str) or nums[i] % n == 0:
        pass
      else:
        # sign: direction +- of this circle
        sign = 1 if nums[i] > 0 else -1
        # indicate path start from i with str(i)
        j = i
        # break if next is visited, reverse direction or self-loop
        while isinstance(nums[j], int) and nums[j] * sign > 0 and nums[j] % n:
          # index of next 
          jnext = (j + nums[j]) % n
          # mark this one as part of path indicated by str(i)
          nums[j] = str(i)
          # move to the next
          j = jnext
          # make a circle?
          if nums[j] == str(i):
            return True
      i += 1
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [1],
    [1,1,2,3,5,8],
    [-1,-2,-3,-4,-5],
  ]
  rslts = [solver.circularArrayLoop(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
