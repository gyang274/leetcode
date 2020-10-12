class Solution:
  def longestPrefix(self, s: str) -> str:
    # rolling hash
    # use large prime as hash function, pay attention to the possible hash collision.
    # fibonacci primes: 2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437, 2971215073, 
    #  99194853094755497, 1066340417491710595814572169, 19134702400093278081449423917, ..
    M = 19134702400093278081449423917
    n, h, t = len(s), 0, 0
    v = list(map(lambda x: ord(x) - ord('a'), s))
    l, p = 0, 1
    for i in range(n - 1):
      h = (h * 26 + v[i]) % M
      t = (v[n - 1 - i] * p + t) % M
      p = p * 26 % M
      if h == t:
        l = i + 1
    return s[:l]

class Solution:
  def longestPrefix(self, s: str) -> str:
    # KMP
    n = len(s)
    # construct the \pi reference table
    u = [-1 for _ in range(n + 1)]
    k = -1
    for i in range(1, n + 1):
      while k >= 0 and s[k] != s[i - 1]:
        k = u[k]
      k += 1
      u[i] = k
    return s[:u[-1]]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "a",
    "aa",
    "aaa",
    "abab",
    "level",
    "ababab",
    "leetcodeleet",
  ]
  rslts = [solver.longestPrefix(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
