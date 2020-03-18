from typing import List

class NumArray:
  """Sqrt Decomposition, TC: O(sqrt(N)).
  """
  def __init__(self, nums: List[int]):
    return None

  def update(self, i: int, val: int) -> None:
    return None

  def sumRange(self, i: int, j: int) -> int:
    return None

class NumArray:
  """Segment Tree: https://en.wikipedia.org/wiki/segment_tree, TC: O(logN).
  """
  def __init__(self, nums: List[int]):
    self.n = len(nums)
    # segment tree
    # self.st, implement using length 2n instead of 2n - 1, 
    # purposely leave index 0 unused, and use index 1 as root.
    self.st = [None] * self.n + nums
    for i in range(self.n - 1, 0, -1):
      self.st[i] = self.st[2 * i] + self.st[2 * i + 1]
    
  def update(self, i: int, val: int) -> None:
    k, diff = self.n + i, val - self.st[self.n + i]
    while k > 0:
      self.st[k] += diff
      k //= 2
    return None
    
  def sumRange(self, i: int, j: int) -> int:
    l, r, xsum = self.n + i, self.n + j, 0
    while l <= r:
      # l move up along tree
      if l % 2 == 0:
        # if left is left child, the parent will include only inside boundary,
        # so simply move up, and parent and later sum will include what's here
        l //= 2
      else:
        # if left is the right child, then parent will include outside boundary,
        # so add itself, and move right one step (become next parent's left child) and then move up
        xsum += self.st[l]
        l = (l + 1) // 2
      # r move up along tree
      if r % 2 == 1:
        # if right is right child, the parent will include only inside boundary,
        # so simply move up, and parent and later sum will include what's here
        r //= 2
      else:
        # if right is the left child, then parent will include outside boundary,
        # so add itself, and move left one step (become next parent's right child) and then move up
        xsum += self.st[r]
        r = (r - 1) // 2
    return xsum

if __name__ == '__main__':
  # test1
  solver = NumArray([1,2,3,4,5,6,7,8])
  cases = [
    ("sumRange", 3, 5),
    ("update", 0, 2),
    ("sumRange", 3, 5),
    ("sumRange", 0, 5),
    ("update", 4, 2),
    ("sumRange", 3, 5),
    ("sumRange", 2, 7),
  ]
  rslts = [eval(f"solver.{action}(*{param})") for action, *param in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
  # test2
  solver = NumArray([7,2,4,3,5])
  cases = [
    ("update", [4,6]),
    ("update", [0,2]),
    ("update", [0,9]),
    ("sumRange", [4,4]),
    ("update", [3,8]),
    ("sumRange", [0,4]),
    ("update", [4,1]),
    ("sumRange", [0,3]),
    ("sumRange", [0,4]),
    ("update", [2,8]),
    ("sumRange", [2,4]),
  ]
  rslts = [eval(f"solver.{action}(*{param})") for action, param in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")