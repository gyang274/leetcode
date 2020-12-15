class Solution:
  def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
    # TC: O(NlogN), SC: O(1)
    # greedily choose the stone with the maximum aliceValues[i] + bobValues[i].
    v = sorted(zip(aliceValues, bobValues), key=sum)
    s = sum(a for a, b in v[-1::-2]) - sum(b for a, b in v[-2::-2])
    return s and (-1, 1)[s > 0]