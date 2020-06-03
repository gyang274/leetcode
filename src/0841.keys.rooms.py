from typing import List

class Solution:
  def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    keys, hold = {0}, {0}
    while hold:
      nkey = set()
      for k in hold:
        nkey |= set(rooms[k]) - keys
        keys |= nkey
      hold = nkey
    return len(keys) == len(rooms)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,3],[1,4],[2,3,2,4,1],[],[4,3,2]],
  ]
  rslts = [solver.canVisitAllRooms(rooms) for rooms in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
