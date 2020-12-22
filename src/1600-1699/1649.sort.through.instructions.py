from typing import List

from operator import __add__

class SegmentTree:

  def __init__(self, nums, update, query):
    self.n = len(nums)
    self.tree = [None] * self.n + nums
    for i in range(self.n - 1, 0, -1):
      self.tree[i] = query(self.tree[2 * i], self.tree[2 * i + 1])
    self._update = update
    self._query = query

  def update(self, i: int, val: int) -> None:
    k = self.n + i
    while k > 0:
      self.tree[k] = self._update(self.tree[k], val)
      k //= 2
    return None
    
  def query(self, i: int, j: int) -> int:
    l, r, val = self.n + i, self.n + j, None
    while l <= r:
      # l move up along tree
      if l % 2 == 0:
        # if left is left child, the parent will include only inside boundary,
        # so simply move up, and parent and later sum will include what's here
        l //= 2
      else:
        # if left is the right child, then parent will include outside boundary,
        # so add itself, and move right one step (become next parent's left child) and then move up
        val = self.tree[l] if not val else self._query(val, self.tree[l])
        l = (l + 1) // 2
      # r move up along tree
      if r % 2 == 1:
        # if right is right child, the parent will include only inside boundary,
        # so simply move up, and parent and later sum will include what's here
        r //= 2
      else:
        # if right is the left child, then parent will include outside boundary,
        # so add itself, and move left one step (become next parent's right child) and then move up
        val = self.tree[r] if not val else self._query(val, self.tree[r])
        r = (r - 1) // 2
    return val

class Solution:
  def createSortedArray(self, instructions: List[int]) -> int:
    # segment tree, TC: O(NlogM), SC: O(M), where N = len(A), M = max(A)
    m = max(instructions)
    v = SegmentTree([0] * (m + 2), __add__, __add__)
    s = 0
    for i, x in enumerate(instructions):
      s += min(v.query(0, x - 1), i - v.query(0, x))
      v.update(x, 1)
    return s % (10 ** 9 + 7)

class Solution:
  def createSortedArray(self, instructions: List[int]) -> int:
    # binary index tree, TC: O(NlogM), SC: O(M), where N = len(A), M = max(A)
    # https://www.hackerearth.com/practice/notes/binary-indexed-tree-or-fenwick-tree/
    m = max(instructions)
    v = [0] * (m + 1)
    def update(x):
      while x <= m:
        v[x] += 1
        x += x & -x
    def get(x):
      s = 0
      while x > 0:
        s += v[x]
        x -= x & -x
      return s
    s = 0
    for i, x in enumerate(instructions):
      s += min(get(x - 1), i - get(x))
      update(x)
    return s % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,5,4],
  ]
  rslts = [solver.createSortedArray(instructions) for instructions in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
