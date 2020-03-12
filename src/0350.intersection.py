from collections import Counter

class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    x1 = Counter(nums1)
    x2 = Counter(nums2)
    if len(x1) > len(x2):
      x1, x2 = x2, x1
    x = []
    for k in x1:
      if k in x2:
        x.extend([k] * min(x1[k], x2[k]))
    return x

class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    """one counter/hashmap
    """
    # counter on the shorter one
    if len(nums1) > len(nums2):
      nums1, nums2 = nums2, nums1
    x1 = Counter(nums1)
    # go through the longer one once
    x = []
    for k in nums2:
      if k in x1:
        x1[k] -= 1
        if x1[k] == 0:
          x1.pop(k)
        x.append(k)
    return x