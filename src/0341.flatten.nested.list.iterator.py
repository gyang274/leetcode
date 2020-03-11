# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#   def isInteger(self) -> bool:
#     """
#     @return True if this NestedInteger holds a single integer, rather than a nested list.
#     """
#
#   def getInteger(self) -> int:
#     """
#     @return the single integer that this NestedInteger holds, if it holds a single integer
#     Return None if this NestedInteger holds a nested list
#     """
#
#   def getList(self) -> [NestedInteger]:
#     """
#     @return the nested list that this NestedInteger holds, if it holds a nested list
#     Return None if this NestedInteger holds a single integer
#     """

class NestedIterator:
  def __init__(self, nestedList: [NestedInteger]):
    # stack of index pointing to next in nestedList at each level
    self.stack = [[0, nestedList], ]
    self.inext = None
  def next(self) -> int:
    v = None
    if self.inext is None or self.hasNext():
      v = self.inext
      self.inext = None
    return v
  def hasNext(self) -> bool:
    if self.inext is None:
      while self.stack and self.stack[-1][0] == len(self.stack[-1][1]):
        self.stack.pop()
      while self.stack and not self.stack[-1][1][self.stack[-1][0]].isInteger():
        # in case of [[], [[], []], 1, [2, 3], ..] empty lists..
        self.stack.append([0, self.stack[-1][1][self.stack[-1][0]].getList()])
        self.stack[-2][0] += 1
        while self.stack and self.stack[-1][0] == len(self.stack[-1][1]):
          self.stack.pop()
      if self.stack:  
        self.inext = self.stack[-1][1][self.stack[-1][0]].getInteger()
        self.stack[-1][0] += 1
      else:
        return False
    return True

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
#
# [[], [[], []], 1, [2], [3,[4,[5,6],7,8],9,10], 11]
#
# [
#   NestedInteger{_integer: None, _list: []}, 
#   NestedInteger{_integer: None, _list: [
#     NestedInteger{_integer: None, _list: []},
#     NestedInteger{_integer: None, _list: []}
#   ]},
#   NestedInteger{_integer: 1, _list: []}, 
#   NestedInteger{_integer: None, _list: [
#     NestedInteger{_integer: 2, _list: []}
#   ]},
#   NestedInteger{_integer: None, _list: [
#     NestedInteger{_integer: 3, _list: []}, 
#     NestedInteger{_integer: None, _list: [
#       NestedInteger{_integer: 4, _list: []}, 
#       NestedInteger{_integer: None, _list: [
#         NestedInteger{_integer: 5, _list: []},
#         NestedInteger{_integer: 6, _list: []}
#       ]},
#       NestedInteger{_integer: 7, _list: []},
#       NestedInteger{_integer: 8, _list: []}
#     ]},
#     NestedInteger{_integer: 9, _list: []},
#     NestedInteger{_integer: 10, _list: []}
#   ]},
#   NestedInteger{_integer: 11, _list: []}
# ]
#
# Add 0 in test case
# [[], [[], []], 0, [0], 1, [2], [3,[4,[5,6],7,8],9,10], 11]