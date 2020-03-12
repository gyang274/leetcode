class Solution:
  def reverseVowels(self, s: str) -> str:
    # vowels
    vowels = set([
      'a', 'e', 'i', 'o', 'u',
      'A', 'E', 'I', 'O', 'U'
    ])
    # i, j: two pointers
    i, j, n, s = 0, len(s) - 1, len(s), list(s)
    while i < j:
      while i < n and not s[i] in vowels:
        i += 1
      while j > 0 and not s[j] in vowels:
        j -= 1
      if i < j:
        s[i], s[j] = s[j], s[i]
      i += 1
      j -= 1
    return ''.join(s)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "leetcode",
    "hello world!",
  ]
  rslts = [solver.reverseVowels(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")