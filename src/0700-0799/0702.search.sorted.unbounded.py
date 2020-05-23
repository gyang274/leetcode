# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#   def get(self, index: int) -> int:
#     return array[index] if index < len(array) else 2147483647

class Solution:
  def search(self, reader: "ArrayReader", target: int) -> int:
    MAX_INT = 2147483647
    r, x = 1, reader.get(1)
    while not (x > target or x == MAX_INT):
      if x == target:
        return r
      r *= 2
      x = reader.get(r)
    l = 0
    while l < r:
      m = l + (r - l) // 2
      x = reader.get(m)
      if x == target:
        return m
      elif x < target:
        l = m + 1
      else:
        r = m
    return -1

