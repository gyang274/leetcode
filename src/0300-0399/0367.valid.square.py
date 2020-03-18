class Solution:
  def isPerfectSquare(self, num: int) -> bool:
    """newton's method
    """
    if num < 2:
      return True
    x = num // 2
    while abs(x ** 2 - num) > 1:
      x = (x + num / x) / 2
    x = int(x)
    return x ** 2 == num

class Solution:
  def isPerfectSquare(self, num: int) -> bool:
    """newton's method
    """
    if num < 2:
      return True
    x = num // 2
    while x * x > num:
      x = (x + num // x) // 2
    return x * x == num

if __name__ == '__main__':
  solver = Solution()
  cases = [
    1, 2, 3, 4, 5, 9, 14, 49,
  ]
  rslts = [solver.isPerfectSquare(num) for num in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")