class Solution:
  def wiggleSort(self, nums: List[int]) -> None:
    """Do not return anything, modify nums in-place instead.
      Local switch, only need to make sure nums[i-1] <= nums[i] >= nums[i+1] for i in range(1, len(nums), 2), and then
      the other condition nums[i-1] >= nums[i] <= nums[i+1] for i in range(0, len(nums), 2) will be satisified auto.
    """
    for i in range(1, len(nums), 2):
      if nums[i] < nums[i-1]:
        nums[i], nums[i-1] = nums[i-1], nums[i]
      if i + 1 < len(nums) and nums[i] < nums[i+1]:
        nums[i], nums[i+1] = nums[i+1], nums[i]
