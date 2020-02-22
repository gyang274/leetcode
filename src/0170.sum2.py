class TwoSum:
  """TwoSum
    1. add O(1), find O(N): maintain a list and find as in Q0001.
    2. add O(N), find O(1): maintain a list of element and a set of all possible sum.
    which one to implement should depends on
      1) num of element in total, 2) memory constraint, 3) ratio of add/find operations
  """
  def __init__(self):
    """Initialize your data structure here.
    """
    self.nums = []
    
  def add(self, number: int) -> None:
    """Add the number to an internal data structure..
    """
    self.nums.append(number)
    
  def find(self, value: int) -> bool:
    """Find if there exists any pair of numbers which sum is equal to the value.
    """
    seen = set()
    for x in self.nums:
      if value - x in seen:
        return True
      else:
        seen.add(x)
    return False
