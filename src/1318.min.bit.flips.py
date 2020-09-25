class Solution:
  def minFlips(self, a: int, b: int, c: int) -> int:
    a, b, c = list(map(lambda s: bin(s)[2:], [a, b, c]))
    n = max(map(len, [a, b, c]))
    a, b, c = list(map(lambda s: '0' * (n - len(s)) + s, [a, b, c]))
    return sum(((x == '1') + (y == '1')) if z == '0' else (x == y == '0') for x, y, z in zip(a, b, c))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, 3, 5),
    (2, 4, 7),
  ]
  rslts = [solver.minFlips(a, b, c) for a, b, c in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
