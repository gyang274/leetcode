class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    """naive linear search: O(N^2), sort: O(NlogN), hash table: O(N).
    """
    return len(nums) > len(set(nums))