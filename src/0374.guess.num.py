# The guess API is already defined for you.
# def guess(num: int) -> int:
#   @param num, your guess
#   @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
#   return x

class Solution:
  def guessNumber(self, n: int) -> int:
    """modified binary search.
    """
    l, r = 0, n
    while l <= r:
      m = l + (r - l) // 2
      x = guess(m)
      if x == 0:
        return m
      elif x == -1:
        r = m - 1
      else:
        l = m + 1
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
  ]
  rslts = [solver.guessNumber(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")