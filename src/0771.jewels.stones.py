class Solution:
  def numJewelsInStones(self, J: str, S: str) -> int:
    J = set(J)
    return len([1 for s in S if s in J])
