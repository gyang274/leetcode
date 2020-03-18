from typing import List

class Solution:
  def recursive(self, i1, i2, k):
    if (i1, i2, k) in self.memo:
      return self.memo[(i1, i2, k)]
    # mk: memo key (since k might be modified later)
    mk = (i1, i2, k)
    if k == 0:
      self.memo[mk] = []
    elif i1 == self.n1 or i2 == self.n2:
      # nums are selected from one only one list
      iX, nX, numsX = (i1, self.n1, self.nums1) if i2 == self.n2 else (i2, self.n2, self.nums2)
      # select the max available and possible recursively
      self.memo[mk] = []
      while 0 < k < nX - iX:
        xmax = max(numsX[iX:(nX - (k - 1))])
        iX = iX + numsX[iX:].index(xmax) + 1
        self.memo[mk].append(xmax)
        k -= 1
      if k > 0:
        self.memo[mk].extend(numsX[-k:])
    else:
      # i1 can select from i1 -> min(n1, (i1 + (n1 - i1) + (n2 - i2) - (k - 1)))
      # min(n1, (n1 + (n2 - i2) - (k - 1)))
      x1max = max(self.nums1[i1:(self.n1 + (self.n2 - i2) - (k - 1))])
      i1max = i1 + self.nums1[i1:].index(x1max)
      # i2 can select from i2 -> min(n2, (i2 + (n1 - i1) + (n2 - i2) - (k - 1)))
      # min(n2, (n2 + (n1 - i1) - (k - 1)))
      x2max = max(self.nums2[i2:(self.n2 + (self.n1 - i1) - (k - 1))])
      i2max = i2 + self.nums2[i2:].index(x2max)
      if x1max > x2max:
        self.memo[mk] = [x1max] + self.recursive(i1max + 1, i2, k - 1)
      elif x1max < x2max:
        self.memo[mk] = [x2max] + self.recursive(i1, i2max + 1, k - 1)
      else:
        # x1max == x2max
        # branch on both options
        ans1 = self.recursive(i1max + 1, i2, k - 1)
        ans2 = self.recursive(i1, i2max + 1, k - 1)
        for x1, x2 in zip(ans1, ans2):
          if x1 > x2:
            self.memo[mk] = [x1max] + ans1
            # stop next loop by return directly
            return self.memo[mk]
          elif x1 < x2:
            self.memo[mk] = [x2max] + ans2
            # stop next loop by return directly
            return self.memo[mk]
        # in case x1 == x2 for all
        self.memo[mk] = [x1max] + ans1
    return self.memo[mk]
  def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
    self.nums1, self.n1 = nums1, len(nums1)
    self.nums2, self.n2 = nums2, len(nums2)
    self.memo = {}
    return self.recursive(0, 0, k)

class Solution:
  def singleMaxNumber(self, nums, k):
    ans = []
    i, n = 0, len(nums)
    while 0 < k < n - i:
      x = max(nums[i:(n - (k - 1))])
      i = i + nums[i:].index(x) + 1
      ans.append(x)
      k -= 1
    if k > 0:
      ans.extend(nums[-k:])
    return ans
  def merge(self, nums1, nums2):
    # merger nums1 (size n1) and nums2 (size n2) to largest number (size k = n1 + n2) possible
    return [max(nums1, nums2).pop(0) for _ in nums1 + nums2]
  def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
    return max([
      self.merge(
        self.singleMaxNumber(nums1, n1), self.singleMaxNumber(nums2, k - n1)
      ) for n1 in range(max(0, k - len(nums2)), min(len(nums1), k) + 1)
    ])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([8,9], [3,9], 3),
    ([], [9, 8, 5, 8], 4),
    ([9, 8, 5, 8], [], 2),
    ([6, 7, 5], [4, 8, 1], 3),
    ([5, 5, 1], [4, 0, 1], 3),
    ([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5),
    ([6, 7, 9, 1, 4], [5, 8, 9, 2, 3], 8),
    ([6, 7, 9, 1, 4], [5, 8, 9, 2, 3], 7),
    (
      [
        8,9,7,3,5,9,1,0,8,5,3,0,9,2,7,4,8,9,8,1,0,2,0,2,7,2,3,5,4,7,4,1,4,0,1,4,2,1,3,1,5,3,9,3,9,0,1,7,0,6,1,8,5,6,6,5,
        0,4,7,2,9,2,2,7,6,2,9,2,3,5,7,4,7,0,1,8,3,6,6,3,0,8,5,3,0,3,7,3,0,9,8,5,1,9,5,0,7,9,6,8,5,1,9,6,5,8,2,3,7,1,0,1,
        4,3,4,4,2,4,0,8,4,6,5,5,7,6,9,0,8,4,6,1,6,7,2,0,1,1,8,2,6,4,0,5,5,2,6,1,6,4,7,1,7,2,2,9,8,9,1,0,5,5,9,7,7,8,8,3,
        3,8,9,3,7,5,3,6,1,0,1,0,9,3,7,8,4,0,3,5,8,1,0,5,7,2,8,4,9,5,6,8,1,1,8,7,3,2,3,4,8,7,9,9,7,8,5,2,2,7,1,9,1,5,5,1,
        3,5,9,0,5,2,9,4,2,8,7,3,9,4,7,4,8,7,5,0,9,9,7,9,3,8,0,9,5,3,0,0,3,0,4,9,0,9,1,6,0,2,0,5,2,2,6,0,0,9,6,3,4,1,2,0,
        8,3,6,6,9,0,2,1,6,9,2,4,9,0,8,3,9,0,5,4,5,4,6,1,2,5,2,2,1,7,3,8,1,1,6,8,8,1,8,5,6,1,3,0,1,3,5,6,5,0,6,4,2,8,6,0,
        3,7,9,5,5,9,8,0,4,8,6,0,8,6,6,1,6,2,7,1,0,2,2,4,0,0,0,4,6,5,5,4,0,1,5,8,3,2,0,9,7,6,2,6,9,9,9,7,1,4,6,2,8,2,5,3,
        4,5,2,4,4,4,7,2,2,5,3,2,8,2,2,4,9,8,0,9,8,7,6,2,6,7,5,4,7,5,1,0,5,7,8,7,7,8,9,7,0,3,7,7,4,7,2,0,4,1,1,9,1,7,5,0,
        5,6,6,1,0,6,9,4,2,8,0,5,1,9,8,4,0,3,1,2,4,2,1,8,9,5,9,6,5,3,1,8,9,0,9,8,3,0,9,4,1,1,6,0,5,9,0,8,3,7,8,5
      ],
      [
        7,8,4,1,9,4,2,6,5,2,1,2,8,9,3,9,9,5,4,4,2,9,2,0,5,9,4,2,1,7,2,5,1,2,0,0,5,3,1,1,7,2,3,3,2,8,2,0,1,4,5,1,0,0,7,7,
        9,6,3,8,0,1,5,8,3,2,3,6,4,2,6,3,6,7,6,6,9,5,4,3,2,7,6,3,1,8,7,5,7,8,1,6,0,7,3,0,4,4,4,9,6,3,1,0,3,7,3,6,1,0,0,2,
        5,7,2,9,6,6,2,6,8,1,9,7,8,8,9,5,1,1,4,2,0,1,3,6,7,8,7,0,5,6,0,1,7,9,6,4,8,6,7,0,2,3,2,7,6,0,5,0,9,0,3,3,8,5,0,9,
        3,8,0,1,3,1,8,1,8,1,1,7,5,7,4,1,0,0,0,8,9,5,7,8,9,2,8,3,0,3,4,9,8,1,7,2,3,8,3,5,3,1,4,7,7,5,4,9,2,6,2,6,4,0,0,2,
        8,3,3,0,9,1,6,8,3,1,7,0,7,1,5,8,3,2,5,1,1,0,3,1,4,6,3,6,2,8,6,7,2,9,5,9,1,6,0,5,4,8,6,6,9,4,0,5,8,7,0,8,9,7,3,9,
        0,1,0,6,2,7,3,3,2,3,3,6,3,0,8,0,0,5,2,1,0,7,5,0,3,2,6,0,5,4,9,6,7,1,0,4,0,9,6,8,3,1,2,5,0,1,0,6,8,6,6,8,8,2,4,5,
        0,0,8,0,5,6,2,2,5,6,3,7,7,8,4,8,4,8,9,1,6,8,9,9,0,4,0,5,5,4,9,6,7,7,9,0,5,0,9,2,5,2,9,8,9,7,6,8,6,9,2,9,1,6,0,2,
        7,4,4,5,3,4,5,5,5,0,8,1,3,8,3,0,8,5,7,6,8,7,8,9,7,0,8,4,0,7,0,9,5,8,2,0,8,7,0,3,1,8,1,7,1,6,9,7,9,7,2,6,3,0,5,3,
        6,0,5,9,3,9,1,1,0,0,8,1,4,3,0,4,3,7,7,7,4,6,4,0,0,5,7,3,2,8,5,1,4,5,8,5,6,7,5,7,3,3,9,6,8,1,5,1,1,1,0,3
      ],
      500
    ),
  ]
  rslts = [solver.maxNumber(nums1, nums2, k) for nums1, nums2, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")