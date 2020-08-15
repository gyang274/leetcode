from typing import List
from functools import reduce

import operator

class Solution:
  def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
    # n: num skills
    n = len(req_skills)
    # z: target
    z = (1 << n) - 1
    # rs: hash of skill to integer 
    rs = {x: 1 << i for i, x in enumerate(req_skills)}
    # ps: hash people skill to integer
    ps = list(map(lambda p: reduce(operator.__or__, map(lambda s: rs[s], p), 0), people))
    # d: skillset to smallest sufficient team
    d = {0: []}
    # O(2^N M), N = num of skills, M = num of people
    for i, s in enumerate(ps):
      p = {}
      for x in d:
        y = x | s
        if y not in p or len(d[x]) < len(p[y]):
          p[y] = d[x] + [i]
      for y in p:
        if y not in d or len(p[y]) < len(d[y]):
          d[y] = p[y]
    return d[z]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["java","nodejs","reactjs"], [["java"],["nodejs"],["nodejs","reactjs"]]),
    (["algorithms","math","java","reactjs","csharp","aws"], [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]),
  ]
  rslts = [solver.smallestSufficientTeam(req_skills, people) for req_skills, people in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
