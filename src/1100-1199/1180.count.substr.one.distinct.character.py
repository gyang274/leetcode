class Solution:
  def countLetters(self, S: str) -> int:
    # two pointers
    i, j, n, count = 0, 0, len(S), 0
    while i < n:
      while j < n and S[i] == S[j]:
        j += 1
      count += (j - i + 1) * (j - i) // 2
      i = j
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "aaaza", "aaaaaaaaaa",
  ]
  rslts = [solver.countLetters(S) for S in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
