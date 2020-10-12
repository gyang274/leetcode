class Solution:
  def getNoZeroIntegers(self, n: int) -> List[int]:
    return next([x, n-x] for x in range(n) if '0' not in f'{x}{n-x}')