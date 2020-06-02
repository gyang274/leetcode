class Solution:
  def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    return [[1 - x for x in r[::-1]] for r in A]
