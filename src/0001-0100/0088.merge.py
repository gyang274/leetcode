from typing import List


class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """Do not return anything, modify nums1 in-place instead.
      Key: go from ende to init, largest should be place at the ende.
    """
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
      if i < 0 or nums1[i] < nums2[j]:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1
      else:
        nums1[k] = nums1[i]
        k -= 1
        i -= 1
    return None


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ([], 0, [], 0),
    ([1], 1, [], 0),
    ([0], 0, [1], 1),
    ([2,0], 1, [1], 1),
    ([1,2,3,0,0,0], 3, [2,5,6], 3)
  ]
  rslts = [solver.merge(nums1, m, nums2, n) for (nums1, m, nums2, n) in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
