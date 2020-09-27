from typing import List

class Solution:
  def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
    return [x[1] for x in sorted([(r[1], r[0]) for r in restaurants if r[2] >= veganFriendly and r[3] <= maxPrice and r[4] <= maxDistance], reverse=True)]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], 1, 50, 10),
    ([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], 0, 50, 10),
  ]
  rslts = [solver.filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance) for restaurants, veganFriendly, maxPrice, maxDistance in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
