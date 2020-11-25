from typing import List
from collections import defaultdict, deque

class Solution:
  def alertNames(self, name: List[str], time: List[str]) -> List[str]:
    # convert time into minutes of the day
    TN = sorted(zip(list(map(lambda x: int(x[:2]) * 60 + int(x[-2:]), time)), name))
    # O(N), one pass
    d, s = defaultdict(deque), set()
    for y, x in TN:
      while d[x] and (d[x][0] > y or d[x][0] < y - 60):
        d[x].popleft()
      d[x].append(y)
      if len(d[x]) > 2:
        s.add(x)
    return sorted(s)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["john","john","john"], ["23:58","23:59","00:01"]),
    (["alice","alice","alice","bob","bob","bob","bob"], ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]),
    (["daniel","daniel","daniel","luis","luis","luis","luis"], ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]),
    (["leslie","leslie","leslie","clare","clare","clare","clare"], ["13:00","13:20","14:00","18:00","18:51","19:30","19:49"]),
    (["a","a","a","a","a","b","b","b","b","b","b"], ["23:20","11:09","23:30","23:02","15:28","22:57","23:40","03:43","21:55","20:38","00:19"]),
    (["a","a","a","a","b","b","b","b","b","b","c","c","c","c"], ["01:35","08:43","20:49","00:01","17:44","02:50","18:48","22:27","14:12","18:00","12:38","20:40","03:59","22:24"]),
  ]
  rslts = [solver.alertNames(name, time) for name, time in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
