from typing import List

class Solution:
  def videoStitching(self, clips: List[List[int]], T: int) -> int:
    # greedy
    clips.sort()
    count, xe, ne = 0, 0, None
    for cs, ce in clips:
      if cs > xe:
        if not ne:
          return -1
        count += 1
        xe, ne = ne, None
      if cs <= xe:
        if not ne or ce > ne:
          ne = ce
      if xe >= T:
        return count
    if ne:
      count += 1
      xe, ne = ne, None
    if xe >= T:
      return count
    return -1

class Solution:
  def videoStitching(self, clips: List[List[int]], T: int) -> int:
    # greedy
    # xe, ne: current included ende, and next included ende
    count, xe, ne = 0, -1, 0
    # cs, ce: clip start, and clip ende
    for cs, ce in sorted(clips):
      if ne >= T or cs > ne:
        break
      elif xe < cs <= ne:
        count += 1
        xe = ne
      ne = max(ne, ce)
    return count if ne >= T else -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[0,1],[1,2]], 5),
    ([[0,4],[2,8]], 5),
    ([[0,4],[5,8]], 5),
    ([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10),
    ([[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], 9),
  ]
  rslts = [solver.videoStitching(clips, T) for clips, T in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
