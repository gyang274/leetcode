class Solution:
  def mfib(self, n):
    """modified fibonacci: f(0) = 1, f(1) = 2, f(n) = f(n - 1) + f(n - 2).
      count num of binary w.o. consecutive 1s w.o. constraint up n digits.
    """
    return int(((((1 + 5 ** 0.5) / 2) ** (n + 2) - ((1 - 5 ** 0.5) / 2) ** (n + 2))) / (5 ** 0.5))
  def findIntegers(self, num: int) -> int:
    """if no constraint, f(n) = self.mfib(n).
      once saw 11xxxx -> 101010 will be the upper bound, say 1000110000 -> 1000101010.
    """
    num = list(bin(num)[2:])
    n, count = len(num), 1
    for i in range(n):
      if num[i] == "1":
        if i == 0 or num[i - 1] == "0":
          count += self.mfib(n - 1 - i)
        elif i + 1 < n:
          for j in range(i + 1, n, 2):
            count += self.mfib(n - 1 - j)
          break
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    0, 1, 2, 3, 5, 8, 12, 42, 85, 1548,
  ]
  rslts = [solver.findIntegers(num) for num in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")