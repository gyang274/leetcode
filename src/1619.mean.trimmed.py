from typing import List

class Solution:
  def trimMean(self, arr: List[int]) -> float:
    return mean(sorted(arr)[(len(arr) // 20):(len(arr) * 19 // 20)])
