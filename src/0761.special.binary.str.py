class Solution:
  def makeLargestSpecial(self, S: str) -> str:
    """O(N^2): recursion.
      split S into several special strings (as many as possible).
      special string starts with 1 and ends with 0. Recursion on the middle part.
      sort all special strings in lexicographically largest order.
      join and output all strings.
    """
    # b: balance of 1 - 0
    i, b, ans = 0, 0, []
    for j, v in enumerate(S):
      b += 1 if v == '1' else -1
      if b == 0:
        ans.append('1' + self.makeLargestSpecial(S[(i + 1):j]) + '0')
        i = j + 1
    return ''.join(sorted(ans, reverse=True))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "11011000",
    "11011000111000",
  ]
  rslts = [solver.makeLargestSpecial(S) for S in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")

        