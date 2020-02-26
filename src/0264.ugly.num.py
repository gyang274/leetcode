class Solution:
  def nthUglyNumber(self, n: int) -> int:
    """Keep 3 pointers on the candidates to get next ugly number by x2, x3, x5.
    """
    nums, i2, i3, i5 = [1], 0, 0, 0
    while len(nums) < n:
      # move to next x2
      while nums[i2] * 2 <= nums[-1]:
        i2 += 1
      x2 = nums[i2] * 2
      # move to next x3
      while nums[i3] * 3 <= nums[-1]:
        i3 += 1
      x3 = nums[i3] * 3
      # move to next x5
      while nums[i5] * 5 <= nums[-1]:
        i5 += 1
      x5 = nums[i5] * 5
      # append min(x2, x3, x5) to nums
      if x2 < x3 and x2 < x5:
        nums.append(x2)
        i2 += 1
      elif x3 < x5:
        # x3 < x5 and x3 < x2:
        nums.append(x3)
        i3 += 1
      else:
        # x5 < x3 and x5 < x2:
        nums.append(x5)
        i5 += 1
    return nums[-1]

class Solution:
  def nthUglyNumber(self, n):
    """Keep 3 pointers on the candidates to get next ugly number by x2, x3, x5.
    """
    # allocate nums memory for length n all at once
    nums, i2, i3, i5 = [1] * n, 0, 0, 0
    for j in range(1, n):
      # move to next x2
      while nums[i2] * 2 <= nums[j-1]:
        i2 += 1
      x2 = nums[i2] * 2
      # move to next x3
      while nums[i3] * 3 <= nums[j-1]:
        i3 += 1
      x3 = nums[i3] * 3
      # move to next x5
      while nums[i5] * 5 <= nums[j-1]:
        i5 += 1
      x5 = nums[i5] * 5
      # append min(x2, x3, x5) to nums
      if x2 < x3 and x2 < x5:
        nums[j] = x2
        i2 += 1
      elif x3 < x5:
        # x3 < x5 and x3 < x2:
        nums[j] = x3
        i3 += 1
      else:
        # x5 < x3 and x5 < x2:
        nums[j] = x5
        i5 += 1
    return nums[-1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    1, 2, 3, 5, 8, 10, 42, 85,
  ]
  rslts = [solver.nthUglyNumber(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")