class Solution:
  def validWordAbbreviation(self, word: str, abbr: str) -> bool:
    i, j = 0, 0
    while i < len(abbr) and j < len(word):
      if abbr[i].isdigit() and not (abbr[i] == "0"):
        k = 1
        while i + k < len(abbr) and abbr[i + k].isdigit():
          k += 1
        j += int(abbr[i:(i + k)])
        i += k
      elif abbr[i] == word[j]:
        j += 1
        i += 1
      else:
        return False
    return i == len(abbr) and j == len(word)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("", ""),
    ("", "0"),
    ("", "1"),
    ("a", "01"),
    ("word", "4"),
    ("word", "w3"),
    ("word", "3d"),
    ("word", "w2d"),
    ("helloword", "h7d"),
    ("helloword", "h7ds"),
    ("helloword!", "h7d"),
    ("helloword!", "h7d!"),
    ("internationalization", "i18n"),
    ("internationalization", "i12iz4n"),
  ]
  rslts = [solver.validWordAbbreviation(word, abbr) for word, abbr in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")