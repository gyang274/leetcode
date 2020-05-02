class MyHashSet:

  def __init__(self):
    """Initialize your data structure here.
    """
    self.nums = [0] * 1000001

  def add(self, key: int) -> None:
    self.nums[key] = 1

  def remove(self, key: int) -> None:
    self.nums[key] = 0

  def contains(self, key: int) -> bool:
    """Returns true if this set contains the specified element
    """
    return self.nums[key] == 1

# NOTE
# hash function: dynamic array size as num of keys, account cost of rehashing and redistributing the existing values.
# collision handling: separate chaining, open addressing, 2-choice hashing bucket size θ(log(log(n))).