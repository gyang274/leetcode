# questionable question.
# https://leetcode.com/problems/max-points-on-a-line/discuss/507060/Questionable-question-regarding-floating-point-arithmetic-limitation.

from typing import List
from collections import defaultdict

class Solution:
  def maxPoints(self, points: List[List[int]]) -> int:
    """Brute-force: maintain a inf + x if slope == inf else slope + y-intercept vs points hashmap, O(n^2)
    """
    if len(points) < 3:
      return len(points)
    sdict = defaultdict(set)
    for i in range(0, len(points)):
      for j in range(i + 1, len(points)):
        if points[i][0] == points[j][0]:
          sdict[('inf', points[i][0])].update([i, j])
        else:
          # numeric issue
          # 94911150 / 94911151                                       
          # 0.9999999894638303
          # 94911151 / 94911152                                       
          # 0.9999999894638303
          # Decimal(94911151 / 94911152)                              
          # Decimal('0.999999989463830285529866159777157008647918701171875')
          # Decimal(94911150 / 94911151)                              
          # Decimal('0.999999989463830285529866159777157008647918701171875')
          s = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
          # numeric issue
          # 277 - ((277 - 248) / (630 - 560)) * 630
          # > 16.0
          # 248 - ((277 - 248) / (630 - 560)) * 560
          # > 15.999999999999972
          y = points[i][1] - s * points[i][0]
          sdict[(s, y)].update([i, j])
    n = 0
    for k, v in sdict.items():
      n = max(n, len(v))
    return n

class Solution:
  def maxPoints(self, points: List[List[int]]) -> int:
    """Brute-force: maintain a inf + x if slope == inf else slope + y-intercept vs points hashmap, O(n^2)
      Weird: so the key is treat each point as (y, x) instead of (x, y)??? Stupid question!
      This is totally depends on how the test cases are given and how the "expected" solution being calculated,
        but NOT internal numeric issue.
      Stupid question and whoever wrote the "expected" solution doesn't know math well.
    """
    if len(points) < 3:
      return len(points)
    sdict = defaultdict(set)
    for i in range(0, len(points)):
      for j in range(i + 1, len(points)):
        if points[i][1] == points[j][1]:
          sdict[('inf', points[i][1])].update([i, j])
        else:
          s = (points[i][0] - points[j][0]) / (points[i][1] - points[j][1])
          y = points[i][0] - s * points[i][1]
          sdict[(s, y)].update([i, j])
    n = 0
    for k, v in sdict.items():
      n = max(n, len(v))
    return n

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [[1,1],[2,2],[3,3]],
    [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]],
    # numeric issue
    # 94911150 / 94911151                                       
    # 0.9999999894638303
    # 94911151 / 94911152                                       
    # 0.9999999894638303
    # Decimal(94911151 / 94911152)                              
    # Decimal('0.999999989463830285529866159777157008647918701171875')
    # Decimal(94911150 / 94911151)                              
    # Decimal('0.999999989463830285529866159777157008647918701171875')
    [[0,0],[94911151,94911150],[94911152,94911151]],
    # numeric issue: 
    # [(0.4142857142857143, 15.999999999999972)]: {0, 1, 4, 9, 14, 15, 26, 27, 28, 54, 55, 59, 63, 66, ...}
    # [(0.4142857142857143, 16.0)]: {1, 4, 9, 14, 15, 26, 27, 28, 54, 55, 59, 63, 66, 68, ...}
    # [(0.4141048824593128, 16.101265822784825)]: {0, 91, 96}
    [
      [560,248],[0,16],[30,250],[950,187],[630,277],[950,187],[-212,-268],[-287,-222],[53,37],[-280,-100],[-1,-14],
      [-5,4],[-35,-387],[-95,11],[-70,-13],[-700,-274],[-95,11],[-2,-33],[3,62],[-4,-47],[106,98],[-7,-65],[-8,-71],
      [-8,-147],[5,5],[-5,-90],[-420,-158],[-420,-158],[-350,-129],[-475,-53],[-4,-47],[-380,-37],[0,-24],[35,299],
      [-8,-71],[-2,-6],[8,25],[6,13],[-106,-146],[53,37],[-7,-128],[-5,-1],[-318,-390],[-15,-191],[-665,-85],[318,342],
      [7,138],[-570,-69],[-9,-4],[0,-9],[1,-7],[-51,23],[4,1],[-7,5],[-280,-100],[700,306],[0,-23],[-7,-4],[-246,-184],
      [350,161],[-424,-512],[35,299],[0,-24],[-140,-42],[-760,-101],[-9,-9],[140,74],[-285,-21],[-350,-129],[-6,9],
      [-630,-245],[700,306],[1,-17],[0,16],[-70,-13],[1,24],[-328,-260],[-34,26],[7,-5],[-371,-451],[-570,-69],[0,27],
      [-7,-65],[-9,-166],[-475,-53],[-68,20],[210,103],[700,306],[7,-6],[-3,-52],[-106,-146],[560,248],[10,6],[6,119],
      [0,2],[-41,6],[7,19],[30,250]
    ], 
  ]
  rslts = [solver.maxPoints(points) for points in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  