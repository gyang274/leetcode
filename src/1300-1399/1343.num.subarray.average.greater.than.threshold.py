from typing import List

class Solution:
  def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
    n, s, t = len(arr), sum(arr[:k]), threshold * k
    count = 1 if s >= t else 0
    for i in range(k, n):
      s += arr[i] - arr[i - k]
      if s >= t:
        count += 1
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,3,1,1,4], 2, 3),
    ([3,2,1,0,4], 3, 2),
  ]
  rslts = [solver.numOfSubarrays(arr, k, threshold) for arr, k, threshold in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
