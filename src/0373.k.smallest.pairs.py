from typing import List

import heapq

class Solution:
  def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    n1, n2 = len(nums1), len(nums2)
    # boundary
    if n1 == 0 or n2 == 0:
      return []
    # build the priority queue key by sum (u, v)
    i, q, s = 0, [], float('-inf')
    heapq.heapify(q)
    # set up the baseline
    while i < n1:
      j = 0
      while j < n2:
        r = nums1[i] + nums2[j]
        if len(q) < k or r <= s:
          s = max(s, r)
          heapq.heappush(q, (r, (nums1[i], nums2[j])))
        if len(q) >= k and r > s:
          break
        j += 1
      i += 1
    # build the k-smallest
    x = []
    while q and len(x) < k:
      x.append(heapq.heappop(q)[1])
    return x

class Solution:
  def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    n1, n2 = len(nums1), len(nums2)
    # boundary
    if n1 == 0 or n2 == 0:
      return []
    # build the priority queue key by sum (u, v)
    visited, q, x = set([(0, 0), ]), [(nums1[0] + nums2[0], 0, 0), ], []
    heapq.heapify(q)
    # add one at a time  
    while (len(x) < k) and q:
      _, i, j = heapq.heappop(q)
      if i + 1 < n1 and (i + 1, j) not in visited:
        heapq.heappush(q, (nums1[i + 1] + nums2[j], i + 1, j))
        visited.add((i + 1, j))
      if j + 1 < n2 and (i, j + 1) not in visited:
        heapq.heappush(q, (nums1[i] + nums2[j + 1], i, j + 1))
        visited.add((i, j + 1))
      x.append((nums1[i], nums2[j]))
    return x

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([], [], 1),
    ([1,2], [3], 3),
    ([1,1,2], [1,2,3], 2),
    ([1,1,2], [1,2,3], 3),
    ([1,1,2], [1,2,3], 5),
    ([1,1,2], [1,2,3], 8),
    ([1,1,2], [1,2,3], 10),
  ]
  rslts = [solver.kSmallestPairs(nums1, nums2, k) for nums1, nums2, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")