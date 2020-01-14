class Solution:
  def reverse(self, x: int) -> int:
    INT_MAX = 2 ** 31 - 1
    INT_MIN = - 2 ** 31
    sign = 1 if x > 0 else -1
    x = x if x > 0 else -x
    z = 0
    while x > 0:
      r = x % 10
      if z > INT_MAX // 10:
        return 0
      elif sign > 0 and z == INT_MAX // 10 and r > 7:
        return 0
      elif sign < 0 and z == INT_MAX // 10 and r > 8:
        return 0
      z = z * 10 + r
      x //= 10      
    return sign * z


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    42, -42, 120, 0, -1, 1, 7463847412, 8463847412, -7463847412, -8463847412, -9463847412
  ]
  rslts = [solver.reverse(x) for x in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")