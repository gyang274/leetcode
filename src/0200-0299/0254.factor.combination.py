from typing import List

class Solution:
  def recusive(self, prefix, fmin, n):
    """Args:
      fmin: min factor, in recursive, control the fmin to eliminate repeatition.
    """
    for i in range(fmin, int(n ** 0.5) + 1):
      if n % i == 0:
        self.ans.append(prefix + [i, n // i])
        self.recusive(prefix + [i], i, n // i)
        
  def getFactors(self, n: int) -> List[List[int]]:
    """Q0039 backtrack.
    """
    self.ans = []
    self.recusive([], 2, n)
    return self.ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    0, 1, 2, 3, 5, 8, 32, 42, 85, 144,
  ]
  rslts = [solver.getFactors(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
        