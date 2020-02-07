class Solution:
  def isScramble(self, s1: str, s2: str) -> bool:
    if not len(s1) == len(s2):
      return False
    # main
    memo = {}
    def recursive(s1, s2):
      # print(f"init: {s1=}, {s2=}")
      if (s1, s2) not in memo:
        n = len(s1)
        if s1 == s2 or (n == 2 and s1[::-1] == s2):
          memo[(s1, s2)] = True
        else:
          memo[(s1, s2)] = False
          for i in range(1, n):
            j = n - i
            # keep at (i, j) split
            memo[(s1, s2)] |= (recursive(s1[:i], s2[:i]) and recursive(s1[i:], s2[i:]))
            if memo[(s1, s2)]:
              break
            # swap at (i, j) split
            memo[(s1, s2)] |= (recursive(s1[:i], s2[j:]) and recursive(s1[i:], s2[:j]))
            if memo[(s1, s2)]:
              break
      # print(f"ende: {s1=}, {s2=}, {memo[(s1, s2)]=}")
      return memo[(s1, s2)]
    return recursive(s1, s2)


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ("", ""),
    ("a", ""),
    ("a", "a"),
    ("ab", "ab"),
    ("ab", "ba"),
    ("ab", "ca"),
    ("abc", "abc"),
    ("abc", "bac"),
    ("abc", "acb"),
    ("abc", "cba"),
    ("abc", "cab"),
    ("abcd", "badc"),
    ("abcd", "cabd"),
    ("great", "rgeat"),
    ("great", "rgtae"),
    ("great", "eatrg"),
    ("abcde", "caebd"),
  ]
  rslts = [solver.isScramble(s1, s2) for s1, s2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")