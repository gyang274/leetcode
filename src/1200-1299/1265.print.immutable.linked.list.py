# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#   def printValue(self) -> None: # print the value of this node.
#   def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
  def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
    ans, node = [], head
    while node:
      ans.append(node)
      node = node.getNext()
    for node in ans[::-1]:
      node.printValue()

# time space algorithm
# O(n), O(n), recursion or use stack
# O(n), O(n^(1/t) + t) for an arbitrary positive integer t, sqrt decomposition
# O(nlgn), O(lgn), divide and conquer
# O(n^2), O(1), load a magazine