from typing import List

class Solution:
  def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
    # TC: O(N), SC: O(1).
    m, n = len(nums1), len(nums2)
    i, j, s1, s2 = 0, 0, 0, 0
    while i < m or j < n:
      if i < m and j < n:
        if nums1[i] == nums2[j]:
          s1 += nums1[i]
          s2 += nums2[j]
          s1 = s2 = max(s1, s2)
          i += 1
          j += 1
        elif nums1[i] < nums2[j]:
          s1 += nums1[i]
          i += 1
        else:
          s2 += nums2[j]
          j += 1
      elif i < m:
        s1 += nums1[i]
        i += 1
      else:
        s2 += nums2[j]
        j += 1
    return max(s1, s2) % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([4,6,8,9], [2,4,5,8,10]),
  ]
  rslts = [solver.maxSum(nums1, nums2) for nums1, nums2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
