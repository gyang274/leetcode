from typing import List
from collections import Counter

class Solution:
  def numRabbits(self, answers: List[int]) -> int:
    d = Counter(answers)
    return sum((d[i] // (i + 1) + (1 if d[i] % (i + 1) else 0)) * (i + 1) for i in d)

class Solution:
  def numRabbits(self, answers: List[int]) -> int:
    count = collections.Counter(answers)
    return sum(-v % (k + 1) + v for k, v in count.items())