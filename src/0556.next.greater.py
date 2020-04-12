class Solution:
  def nextGreaterElement(self, n: int) -> int:
    """Q0031, not Q0496 nor Q0503.
    """
    nums = list(str(n))
    m = len(nums)
    i = m - 1
    while i > 0 and nums[i - 1] >= nums[i]:
      i -= 1
    if i == 0:
      return -1
    else:
      j = i
      while j < m and nums[j] > nums[i - 1]:
        j += 1
      nums[i - 1], nums[j - 1] = nums[j - 1], nums[i - 1]
      for k in range((m - i) // 2):
        nums[i + k], nums[m - 1 - k] = nums[m - 1 - k], nums[i + k]
      z = int("".join(nums)) 
      return z if z < (1 << 31 - 1) else -1
  
if __name__ == '__main__':
  solver = Solution()
  cases = [
    12, 21, 11687654,
  ]
  rslts = [solver.nextGreaterElement(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
