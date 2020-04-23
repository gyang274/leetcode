class Solution:
  def countSubstrings(self, s: str) -> int:
    """Q0005, manacher algorithm.
    """
    n = 2 * len(s) + 1
    # augmented s with #
    ss = lambda s, i: s[(i - 1) // 2] if i & 1 else '#'
    # c: center of palindrome with rightmost position
    c = 0
    # r: right of palindrom with rightmost position
    r = 0
    # i: current position under investigation, c <= i <= r
    i = 0
    # j: relfect of i w.r.t c
    # j = lambda i, c: 2 * c - i
    # p: length of palindrome at each position, e.g., r - c at c
    p = [0] * n
    # loop through i w.r.t manacher algorithm
    for i in range(n):
      if r < i:
        c, r = i, i
      # 2 * c - i - p[2 * c - i] == 2 * c - r
      if p[2 * c - i] == r - i:
        while 2 * i - r >= 0 and r < n and ss(s, 2 * i - r) == ss(s, r):
          r += 1
        r -= 1
        c = i
        p[i] = r - i
      else:
        p[i] = min(p[2 * c - i], r - i)
      # print(i, c, r, [ss(s, i) + ':' + str(p[i]) for i in range(n)])
    return sum([(x + 1) // 2 for x in p])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "abc",
    "aaa",
  ]
  rslts = [solver.countSubstrings(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
