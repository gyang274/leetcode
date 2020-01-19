class Solution:
  def say(self, x: str) -> str:
    s = x[0]
    n = 0
    z = ""
    for i in range(len(x)):
      if x[i] == s:
        n += 1
      else:
        z += str(n) + s
        s = x[i]
        n = 1
    z += str(n) + s
    s = x[i]
    return z
  def countAndSay(self, n: int) -> str:
    if n == 1:
      return "1"
    return self.say(self.countAndSay(n - 1))


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    1, 2, 3, 4, 5, 6, 7
  ]
  rslts = [solver.countAndSay(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")