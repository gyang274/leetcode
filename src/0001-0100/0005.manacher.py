class Solution:
  def longestPalindrome(self, s: str) -> str:
    """Manacher Algorithm.
    """
    n = 2 * len(s) + 1
    # augmented s with #
    ss = lambda s, i: s[(i - 1) // 2] if i % 2 else '#'
    # c: center of palindrome with rightmost position
    c = 0
    # r: right of palindrom with rightmost position
    r = 0
    # i: current position under investigation, c <= i <= r
    i = 0
    # j: relfect of i w.r.t c
    # j = lambda i, c: 2 * c - i
    # p: length of palindrome at each position, e.g., r - c at c
    p = [0 for _ in range(n)]
    # loop through i w.r.t manacher algorithm
    mi = -1
    ml = -1
    for i in range(n):
      if (r < i):
        c, r = i, i
      # 2 * c - i - p[2 * c - i] == 2 * c - r
      if p[2 * c - i] == r - i:
        print('in')
        while 2 * i - r >= 0 and r < n and ss(s, 2 * i - r) == ss(s, r):
          r += 1
        r -= 1
        c = i
        p[i] = r - i
      else:
        p[i] = min(p[2 * c - i], r - i)
      if p[i] > ml:
        mi = i
        ml = p[i]
      # print(i, c, r, [ss(s, i) + ':' + str(p[i]) for i in range(n)])
    return s[((mi - ml) // 2):((mi + ml) // 2)]


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    "aba",
    # "aabba",
    # "aababa",
    # "aabbaa"
  ]
  rslts = [solver.longestPalindrome(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  
