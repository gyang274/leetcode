from typing import List


# singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
  def __repr__(self):
    return str(self.val)
  def __lt__(self, other):
    if isinstance(other, self.__class__):
      return self.val < other.val
  def __le__(self, other):
    if isinstance(other, self.__class__):
      return self.val <= other.val
  def __eq__(self, other):
    if isinstance(other, self.__class__):
      return self.val == other.val
  def __ne__(self, other):
    if isinstance(other, self.__class__):
      return self.val != other.val
  def __ge__(self, other):
    if isinstance(other, self.__class__):
      return self.val >= other.val
  def __gt__(self, other):
    if isinstance(other, self.__class__):
      return self.val > other.val
  def copy(self):
    x = ListNode(self.val)
    x.next = self.next
    return x


def listToListNode(x: List) -> ListNode:
  s = ListNode(0)
  n = s
  for v in x:
    n.next = ListNode(v)
    n = n.next
  return s.next


def traverseListNode(l: ListNode):
  s = ''
  while l:
    s += str(l.val) + ' -> '
    l = l.next
  if len(s) > 0:
    s = s[:-3]
  return s
