# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#   def __init__(self, value=None):
#     """
#     If value is not specified, initializes an empty list.
#     Otherwise initializes a single integer equal to value.
#     """
#
#   def isInteger(self):
#     """
#     @return True if this NestedInteger holds a single integer, rather than a nested list.
#     :rtype bool
#     """
#
#   def add(self, elem):
#     """
#     Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#     :rtype void
#     """
#
#   def setInteger(self, value):
#     """
#     Set this NestedInteger to hold a single integer equal to value.
#     :rtype void
#     """
#
#   def getInteger(self):
#     """
#     @return the single integer that this NestedInteger holds, if it holds a single integer
#     Return None if this NestedInteger holds a nested list
#     :rtype int
#     """
#
#   def getList(self):
#     """
#     @return the nested list that this NestedInteger holds, if it holds a nested list
#     Return None if this NestedInteger holds a single integer
#     :rtype List[NestedInteger]
#     """

class Solution:
  def __init__(self):
    self.depth = 1
    # self.uwxsum: unweighted sum
    # so whenenver encounter a deeper level, +uwxsum of earlier
    self.uwxsum = 0
    # self.xsum: weighted sum
    # this is the weighted sum w.r.t current explore depth
    self.xsum = 0
  def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
    self.depth -= 1
    if self.depth == 0:
      self.depth += 1
      self.xsum += self.uwxsum
    for ni in nestedList:
      if ni.isInteger():
        self.uwxsum += ni.getInteger()
        self.xsum += self.depth * ni.getInteger()
      else:
        self.depthSumInverse(ni.getList())
        self.depth += 1
    return self.xsum

class Solution:
  def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
    """BFS
    """
    # us: unweighted sum
    # ws: weighted sum w.r.t inverse depth
    us, ws, nestedListNextDepth = 0, 0, []
    while nestedList:
      for ni in nestedList:
        if ni.isInteger():
          us += ni.getInteger()
        else:
          nestedListNextDepth.extend(ni.getList())
      ws += us
      nestedList, nestedListNextDepth = nestedListNextDepth, []
    return ws