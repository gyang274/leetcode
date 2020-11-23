# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#   # Compares the sum of arr[l..r] with the sum of arr[x..y]
#   # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#   # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#   # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#   def compareSub(self, l: int, r: int, x: int, y: int) -> int:

#   # Returns the length of the array
#   def length(self) -> int:

class Solution:
  def getIndex(self, reader: 'ArrayReader') -> int:
    # modified binary search
    n = reader.length()
    i, j = 0, n - 1
    while i < j:
      k = j - i + 1
      l, r, x, y = i, i + (k // 2 - 1), j - (k // 2 - 1), j
      z = reader.compareSub(l, r, x, y)
      if z == 0:
        # must be k & 1 = 1
        return i + (k // 2)
      elif z > 0:
        i, j = l, r
      else:
        i, j = x, y
    return i
