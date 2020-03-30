class Solution:
  def recursive(self, s):
    if s not in self.memo:
      n = len(s)
      # find repetitive substr
      candidates = [s]
      # encode s into k[substr]
      i = (s + s).find(s, 1)
      if -1 < i < n:
        candidates.append(str(n // i) + "[" + self.recursive(s[:i]) + "]")
      # encode s into k1[substr1]..kj[substrj]
      for i in range(1, n):
        candidates.append(
          self.recursive(s[:i]) + self.recursive(s[i:])
        )
      self.memo[s] = min(candidates, key=len)
    return self.memo[s]
  def encode(self, s: str) -> str:
    self.memo = {}
    return self.recursive(s)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "a",
    "aa",
    "aaa",
    "aaaa",
    "aaaaa",
    "aaaaaaaa",
    "abbbabbbcabbbabbbc",
  ]
  rslts = [solver.encode(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")