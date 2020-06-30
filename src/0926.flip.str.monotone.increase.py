from itertools import accumulate

class Solution:
  def minFlipsMonoIncr(self, S: str) -> int:
    n = len(S)
    # suppose S is splitted at i s.t. S[:i] = "0s" and S[i:] = "1s",
    # num of flips is count(S[:i], 1) + count(S[i:], 0), 0 <= i <= n
    l = accumulate(map(int, S), initial=0)
    r = reversed(list(accumulate(map(lambda x: int(x) ^ 1, reversed(S)), initial=0)))
    return min(s0 + s1 for s0, s1 in zip(l, r))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "00110",
    "010110",
    "00011000",
  ]
  rslts = [solver.minFlipsMonoIncr(S) for S in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")