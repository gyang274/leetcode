class Solution:
  def nearestPalindromic(self, n: str) -> str:
    l = len(n)
    m = l // 2
    if l & 1:
      x, y, z = n[:m], n[m], n[(m + 1):]
    else:
      x, y, z = n[:m], "", n[m:]
    # base case: abcxy -> abcba, abcxyz -> abccba
    p0 = x + y + x[::-1]
    # move up: 10987 -> 11011 not 10901
    u1 = str(int(x + y) + 1)
    p1 = u1[:m] + u1[m:] + u1[:m][::-1]
    # move down: 1 -> 0, 11 -> 9, 10 -> 9 not 11, 101 -> 99, 100 -> 99 not 101, 17010 -> 16971 not 17071
    u2 = str(int(x + y) - 1) if int(x + y) - 1 > 0 else ""
    p2 = (u2[:m] + (u2[m:] if len(u2) >= m else "9") + u2[:m][::-1]) or "0"
    # choose between p0, p1, p2
    nn = int(n)
    d0, d1, d2 = abs(int(p0) - nn), abs(int(p1) - nn), abs(int(p2) - nn)
    d0 = d0 if d0 > 0 else float("inf")
    # print(f"{n=}, {p0=}, {p1=}, {p2=}")
    if d2 <= d0 and d2 <= d1:
      return p2
    elif d0 <= d1:
      return p0
    else:
      return p1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "1",
    "10",
    "11",
    "101",
    "111",
    "142",
    "1001",
    "10001",
    "10987",
  ]
  rslts = [solver.nearestPalindromic(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
