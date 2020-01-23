class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    """Simple O(nm) solution."""
    n = len(needle)
    for i in range(0, len(haystack) - n  + 1):
      if haystack[i:(i + n)] == needle:
        return i
    return -1


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ("hello", "ll"),
    ("aaaaa", "ab"),
    ("aaaaaaaaaab", "aaaaab"),
    ("ababababababababababac", "abababac"),
    ("world", ""),
    ("", ""),
  ]
  rslts = [solver.strStr(s, pattern) for s, pattern in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")