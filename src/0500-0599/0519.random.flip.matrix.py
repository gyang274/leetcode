import random

class Solution:

  def __init__(self, n_rows: int, n_cols: int):
    self.nn = n_rows * n_cols
    self.zeros = random.sample([i for i in range(self.nn)], k = self.nn)
    self.rc = lambda i: (i // n_cols, i % n_cols)
    
  def flip(self) -> List[int]:
    """TC: O(1), SC: O(1).
    """
    return self.rc(self.zeros.pop())

  def reset(self) -> None:
    """TC: O(N^2), SC: O(N^2)
    """
    self.zeros = random.sample([i for i in range(self.nn)], k = self.nn)

class Solution:

  def __init__(self, n_rows: int, n_cols: int):
    """TC: O(1), SC: O(min(F, N^2)). TODO: use binary representation to store self.ones?
    """
    self.nn = n_rows * n_cols
    self.rc = lambda i: (i // n_cols, i % n_cols)
    self.n0 = self.nn
    self.ones = {}
    
  def flip(self) -> List[int]:
    # hashmap version of swap seen index with last index at each step, in order to reduce space.
    i = random.randrange(self.n0)
    x = self.ones.get(i, i)
    self.n0 -= 1
    if i < self.n0:
      self.ones[i] = self.ones.pop(self.n0, self.n0)
    return self.rc(x)

  def reset(self) -> None:
    self.n0 = self.nn
    self.ones = {}
