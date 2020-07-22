class Solution:
  def queryString(self, S: str, N: int) -> bool:
    # if N > len(S) * 2:
    #   return False
    s, r = set([0]), set()
    for x in S:
      r = {z << 1 | int(x) for z in r if (z << 1 | int(x)) <= N} | {int(x)}
      s |= r
    return len(s) == N + 1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("0110", 3),
    ("0110", 4),
    ("1100", 4),
  ]
  rslts = [solver.queryString(S, N) for S, N in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
