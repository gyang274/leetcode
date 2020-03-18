import random

class Solution:

  def __init__(self, nums: List[int]):
    self.nums = nums

  def reset(self) -> List[int]:
    """Resets the array to its original configuration and return it.
    """
    return self.nums
    
  def shuffle(self) -> List[int]:
    """Returns a random shuffling of the array.
    """
    runs = self.nums.copy()
    # Fisher-Yates Algorithm
    n = len(runs)
    for i in range(n):
      j = random.randint(i, n - 1)
      runs[i], runs[j] = runs[j], runs[i]
    return runs
