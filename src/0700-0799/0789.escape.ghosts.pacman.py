class Solution:
  def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
    def dist(s, t):
      return abs(s[0] - t[0]) + abs(s[1] - t[1])
    d = dist((0, 0), target)
    return all(d < dist(ghost, target) for ghost in ghosts)
