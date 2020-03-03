# The knows API is already defined for you.
# def knows(a: int, b: int) -> bool:
#   return a bool, whether a knows b

class Solution:
  def findCelebrity(self, n: int) -> int:
    """Key: if a knows b then a is not the celebrity, otherwise b is not the celebrity. Eliminate one every call, O(3N).
    """
    candidates = set([i for i in range(n)])
    # remove one every call
    while len(candidates) >= 2:
      a, b = candidates.pop(), candidates.pop()
      if knows(a, b):
        # a is not the celebrity
        candidates.add(b)
      else:
        # b is not the celebrity
        candidates.add(a)
    # all person in candidates knows no one
    if candidates:
      x = candidates.pop()
      for i in range(n):
        if (not i == x) and (not knows(i, x) or knows(x, i)):
          return -1
      return x
    return -1

class Solution:
  def findCelebrity(self, n: int) -> int:
    # if n == 0:
    #   return -1
    # if n == 1:
    #   return 0
    i, j = 0, 1
    while j < n:
      # keep j > i
      if knows(i, j):
        # i is not the celebrity
        i = j
        j += 1
      else:
        # j is not the celebrity
        j += 1
    # i is the candidate of celebrity
    for j in range(n):
      if (not i == j) and (knows(i, j) or not knows(j, i)):
        return -1
    return i

# TODO: cache calls in while loop and re-use in the for loop, e.g.,
# if 0 is the celebrity, then all n - 2 calls cached will be reused.