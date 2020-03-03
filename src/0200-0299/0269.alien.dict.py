from typing import List
from collections import defaultdict

class Solution:
  def alienOrder(self, words: List[str]) -> str:
    """Each pair [w1, w2, ..] should provide one and at most one order, no info if (a, a), or (a, ab), Then Q0210.
    """
    # precedence and reversed dict, 
    # prep[k] = {v1, v2, ..}, means v1 < k, v2 < k, etc.
    # post[k] = {v1, v2, ..}, means v1 > k, v2 > k, etc.
    wset, prep, post = set([]), defaultdict(set), defaultdict(set)
    for i in range(len(words) - 1):
      wset.update(set(words[i]))
      for x, y in zip(words[i], words[i + 1]):
        if not x == y:
          # implies: x < y
          prep[y].add(x)
          post[x].add(y)
          break
    wset.update(set(words[-1]))
    # make a order schedule like in Q0210
    schedule, boundary = [], [x for x in list(wset) if x not in prep] 
    while boundary:
      y = boundary.pop()
      schedule.append(y)
      if y in post:
        xs = post.pop(y)
        for x in xs:
          prep[x].remove(y)
          if not prep[x]:
            prep.pop(x)
            boundary.append(x)
    if prep:
      return ""
    return "".join(schedule)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["z", "x"],
    ["z", "x", "z"],
    ["za", "zb", "ca", "cb"],
    ["wrt", "wrf", "er", "ett", "rftt"],
  ]
  rslts = [solver.alienOrder(words) for words in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  
