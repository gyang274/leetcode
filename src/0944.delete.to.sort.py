class Solution:
  def minDeletionSize(self, A: List[str]) -> int:
    return sum(list(a) != sorted(a) for a in list(zip(*A)))
