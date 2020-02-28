class Solution:
  def reverseWords(self, s: str) -> str:
    return ' '.join(reversed(s.split()))

class Solution:
  def reverseWords(self, s: str) -> str:
    l, r = 0, len(s) - 1
    while l < r and s[l] == ' ':
      l += 1
    while l < r and s[r] == ' ':
      r -= 1
    sent, word = '', ''
    while l <= r:
      if s[l] == ' ':
        if not word == '':
          sent = word + ' ' + sent
        word = ''
      else:
        word += s[l]
      l += 1
    if not word == '':
      sent = word + ' ' + sent
    return sent[:-1]

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    "",
    "  ",
    "the sky is blue",
    "  hello world!  ",
    "a good   example ",
  ]
  rslts = [solver.reverseWords(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  
  