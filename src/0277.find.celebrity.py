# The knows API is already defined for you.
# def knows(a: int, b: int) -> bool:
#   return a bool, whether a knows b

class Solution:
  def findCelebrity(self, n: int) -> int:
    """Find the one who don't know any one, when verify every one know him/her.
    """
    candidates = set([i for i in range(n)])
    j = 1
    while j < n and candidates:
      for i in candidates: 
        if knows(i, ((i + j) % n)):
          candidates.remove(i)
    # all person in candidates knows no one
    if candidates:
      for i in candidates:
        for j in range(n):
          if not knows(j, i):
            candidates.remove(i)
            break
    return candidates.pop() if candidates else -1

