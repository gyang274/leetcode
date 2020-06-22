from typing import List
from collections import deque

class Solution:
  def numRescueBoats(self, people: List[int], limit: int) -> int:
    people = deque(sorted(people))
    count = 0
    while people:
      count += 1
      p = people.pop()
      if people and limit - p >= people[0]:
        people.popleft()
    return count

class Solution:
  def numRescueBoats(self, people: List[int], limit: int) -> int:
    people.sort()
    i, j, k = 0, len(people), 0
    while i < j:
      k += 1
      j -= 1
      if limit - people[j] >= people[i]:
        i += 1
    return k

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,3,1,1,4], 5),
    ([3,2,1,5,4], 5),
  ]
  rslts = [solver.numRescueBoats(people, limit) for people, limit in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
