class Solution:
  def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
    return set(range(n)) - set(y for x, y in edges)
