from collections import Counter

class Solution:
  def __init__(self):
    self.s = {tuple((k, v) for k, v in sorted(Counter(str(1 << i)).items())) for i in range(32)}   
  def reorderedPowerOf2(self, N: int) -> bool:
    return tuple((k, v) for k, v in sorted(Counter(str(N)).items())) in self.s
