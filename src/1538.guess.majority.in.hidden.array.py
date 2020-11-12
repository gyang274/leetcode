# """
# This is the ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
#   # Compares 4 different elements in the array
#   # return 4 if the values of the 4 elements are the same (0 or 1).
#   # return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
#   # return 0 : if two element have a value equal to 0 and two elements have a value equal to 1.
#   def query(self, a: int, b: int, c: int, d: int) -> int:

#   # Returns the length of the array
#   def length(self) -> int:

from collections import Counter

class Solution:
  def guessMajority(self, reader: 'ArrayReader') -> int:
    # n: length
    n = reader.length()
    # TC: O(N), SC: O(N)
    # let A[0] = 0, 5 comparions to determine A[:5], and use query(i-3,i-2,i-1,i) and query(i-4,i-3,i-2,i-1) to 
    # determine A[i], so each A[i] is determined with 1 query.
    # A: array with A[0] = 0
    A = [0] * n
    # 5 comparions to determine A[:5]
    a = reader.query(0,1,2,3)
    e = reader.query(1,2,3,4)
    if not a == e:
      A[4] = 1
    b = reader.query(0,2,3,4)
    if not b == e:
      A[1] = 1
    c = reader.query(0,1,3,4)
    A[2] = A[1] if b == c else A[1] ^ 1
    d = reader.query(0,1,2,4)
    A[3] = A[2] if c == d else A[2] ^ 1
    # use query(i-3,i-2,i-1,i) and query(i-4,i-3,i-2,i-1) to determine A[i]
    x = e
    for i in range(5, n):
      y = reader.query(i - 3, i - 2, i - 1, i)
      A[i] = A[i - 4] if x == y else A[i - 4] ^ 1
      x = y
    # counter
    d = Counter(A)
    if d[0] == d[1]:
      return -1
    return 0 if d[0] > d[1] else A.index(1)
