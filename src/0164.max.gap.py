from typing import List

class Solution:
  def maximumGap(self, nums: List[int]) -> int:
    """pigeonhole principle:
      given a list of n with max and min, min of max gap is gp = (max - min) / (n - 1), and such gap must happen between
      bucket of [min + i * gp, min + (i + 1) * gp), i = 0, ..., n, and i goes n so that include max to easier calcuation
    """
    n = len(nums)
    if n < 2:
      return 0
    xmin, xmax = min(nums), max(nums)
    size = (xmax - xmin) // (n - 1) + (0 if (xmax - xmin) % (n - 1) == 0 else 1)
    if size == 0:
      return 0
    # print(f"{size=}")
    buckets = [[] for _ in range(n)]
    for x in nums:
      i = (x - xmin) // size
      if not buckets[i]:
        buckets[i] = [x, x]
      elif x < buckets[i][0]:
        buckets[i][0] = x
      elif x > buckets[i][1]:
        buckets[i][1] = x
    # print(f"{buckets=}")
    i, l, gap = 0, buckets[0][1], size
    while i < n:
      if buckets[i]:
        gap = max(gap, buckets[i][0] - l)
        l = buckets[i][1]
      i += 1
    return gap
    
if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [],
    [10],
    [3,6,9,2],
    [1,1,1,1,1],
    [1,10000000],
    [1,1,1,1,1,5,5,5,5,5]
  ]
  rslts = [solver.maximumGap(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")