import heapq

class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
    """Solution:
      1. O(NlogN): Sort + k-th index.
      2. O(NlogK): Heap of k.
      3. Quicksort modified, O(N) average, O(N^2) worst.
    """
    return heapq.nlargest(k, nums)[-1]