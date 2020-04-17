class Solution:
  def findRelativeRanks(self, nums: List[int]) -> List[str]:
    # score and index
    score = sorted([(s, i) for i, s in enumerate(nums)], reverse=True)
    # relative ranks
    ranks = [None] * len(nums)
    for r, (s, i) in enumerate(score[:3]):
      if r == 0:
        ranks[i] = "Gold Medal"
      elif r == 1:
        ranks[i] = "Silver Medal"
      elif r == 2:
        ranks[i] = "Bronze Medal"
      else:
        break
    for r, (s, i) in enumerate(score[3:]):
      ranks[i] = str(r + 4)
    return ranks