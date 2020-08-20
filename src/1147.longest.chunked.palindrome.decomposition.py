class Solution:
  def longestDecomposition(self, text: str) -> int:
    n = len(text)
    # O(N) at each iteration, and O(N^2) overall recursion,
    # however, it is possible to use rolling hash to obtain
    # O(1) at each iteration, and O(N) for overall recursion.
    for i in range(1, n // 2 + 1):
      if text[:i] == text[(n - i):]:
        return 2 + self.longestDecomposition(text[i:(n - i)])
    return 1 if text else 0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "aaa",
    "merchant",
    "antaprezatepzapreanta",
    "ghiabcdefhelloadamhelloabcdefghi",
  ]
  rslts = [solver.longestDecomposition(text) for text in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
