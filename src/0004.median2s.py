from typing import List

"""
  Keynote:
    Let x <- nums1, y <- nums2 with |x| = m, |y| = n, m <= n, realize the median of concat(x, y) simply find i and j,
    such that x[i - 1] <= y[j] and x[i] >= y[j - 1], and i + j == (m + n + 1) // 2, where i in [0, m] and j in [0, n].
  Solution:
    i: number of items in nums1 less than combined median
    j: number of items in nums2 less than combined median
    i + j == (m + n + 1) // 2
    x[i - 1] <= y[j]
    x[i] >= y[j - 1]
  Corner Case:
    i == 0 or i == m
"""
class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    n1 = len(nums1)
    n2 = len(nums2)
    # n1 <= n2
    if n1 > n2:
      n1, nums1, n2, nums2 = n2, nums2, n1, nums1
    # odevity
    odevity = (n1 + n2) % 2
    # main
    imin = 0
    imax = n1
    while imin <= imax:
      i = (imin + imax) // 2
      j = (n1 + n2 + 1) // 2 - i
      if i > 0 and nums1[i - 1] > nums2[j]:
        imax = i - 1
      elif i < n1 and nums1[i] < nums2[j - 1]:
        imin = i + 1
      else:
        # max left
        if i == 0:
          maxl = nums2[j - 1]
        elif j == 0:
          maxl = nums1[i - 1]
        else:
          maxl = max(nums1[i - 1], nums2[j - 1])
        if odevity:
          return maxl
        # min right
        if i == n1:
          minr = nums2[j]
        elif j == n2:
          minr = nums1[i]
        else:
          minr = min(nums1[i], nums2[j])
        return (maxl + minr) / 2.0
      

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1, 3], [2]),
    ([1, 2], [3, 4])
  ]
  rslts = [
    solver.findMedianSortedArrays(nums1, nums2) for nums1, nums2 in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")