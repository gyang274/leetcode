from typing import List
from collections import defaultdict

class Solution:
  def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
    foods = sorted(set(x[2] for x in orders))
    fdict = {f: i for i, f in enumerate(foods)}
    tdict = defaultdict(lambda: [0] * len(foods))
    for x in orders:
      tdict[x[1]][fdict[x[2]]] += 1
    ans = [["Table"] + foods]
    for t in sorted(tdict.keys(), key=lambda x: int(x)):
      ans.append([t] + list(map(lambda x: str(x), tdict[t])))
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]],
    [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]],
  ]
  rslts = [solver.displayTable(orders) for orders in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
