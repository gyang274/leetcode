from typing import List

class Solution:
  def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
    players = sorted((a, s) for a, s in zip(ages, scores))
    # O(N), maintain a list of age up, score down, some total score..
    d = {}
    for a, s in players:
      if (a, s) in d:
        d[(a, s)] += s
      else:
        m = s
        for xa, xs in d:
          if (xa < a and xs <= s) or (xa == a):
            m = max(m, d[(xa, xs)] + s)
        d[(a, s)] = m
    return max(d.values())

class Solution:
  def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
    # sort
    players = sorted((a, s) for a, s in zip(ages, scores))
    # dp..
    f = [0] * len(players)
    for i, (a, s) in enumerate(players):
      f[i] = s
      for j in range(i):
        if players[j][1] <= s:
          f[i] = max(f[i], f[j] + s)
    return max(f)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,3,5], [2,3,4,1]),
    ([4,5,6,5], [2,1,2,1]),
    ([1,3,5,10,15], [1,2,3,4,5]),
  ]
  rslts = [solver.bestTeamScore(scores, ages) for scores, ages in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
