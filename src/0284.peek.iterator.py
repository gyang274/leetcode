# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#   def __init__(self, nums: List[int]):
#     """Initializes an iterator object to the beginning of a list.
#     """
#
#   def hasNext(self) -> bool:
#     """Returns true if the iteration has more elements.
#     """
#
#   def next(self) -> int:
#     """Returns the next element in the iteration.
#     """

class PeekingIterator:
  def __init__(self, iterator: 'Iterator'):
    """Initialize your data structure here.
    """
    # 2020.02.29
    # peeked value when peeked, otherwise None indicates not peeked yet.
    # self.peeked = None
    # 2020.02.29
    # what if iterator itself can return None as value, not only integer? must have a separate self.hasPeeked: bool
    self.hasPeeked = False
    self.peekedValue = None
    # iterator
    self.iterator = iterator

  def peek(self) -> int:
    """Returns the next element in the iteration without advancing the iterator.
    """
    if not self.hasPeeked:
      self.peekedValue = self.iterator.next()
      self.hasPeeked = True
    return self.peekedValue

  def next(self) -> int:
    if self.hasPeeked:
      x = self.peekedValue
      self.peekedValue = None
      self.hasPeeked = False
      return x
    return self.iterator.next()

  def hasNext(self) -> bool:
    return self.hasPeeked or self.iterator.hasNext()