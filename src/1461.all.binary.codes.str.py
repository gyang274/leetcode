class Solution:
  def hasAllCodes(self, s: str, k: int) -> bool:
    return len(set(s[i:(i + k)] for i in range(len(s) - k + 1))) == (1 << k)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("0110", 1),
    ("0110", 2),
    ("00110", 2),
  ]
  rslts = [solver.hasAllCodes(s, k) for s, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
