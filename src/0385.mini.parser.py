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
  def recursive(self, s: str):
    x = NestedInteger()
    if s[0] == "[":
      if s[1] == "]":
        return x, s[2:]
      while s:
        y, s = self.recursive(s[1:])
        x.add(y)
        if s[0] == "]":
          break
      return x, s[1:]
    else:
      i, v = 0, ""
      while i < len(s):
        if s[i] == "," or s[i] == "]":
          break
        v += s[i]
        i += 1
      if not v == "":
        x.setInteger(int(v))
      return x, s[i:]
  def deserialize(self, s: str) -> NestedInteger:
    x, _ = self.recursive(s)
    return x

# "[]"
# "[123]"
# "[123,456]"
# "[123,[456]]"
# "[123,456,789]"
# "[123,[456,[789]]]"
# "[[],123,[[],[[],[[]]],456,[789]]]"

# cheat eval()..
class Solution:
  def deserialize(self, s):
    def nestedInteger(x):
      if isinstance(x, int):
        return NestedInteger(x)
      lst = NestedInteger()
      for y in x:
        lst.add(nestedInteger(y))
      return lst
    return nestedInteger(eval(s))
