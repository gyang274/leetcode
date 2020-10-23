class Solution:
  def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
    words, m = sentence.split(), len(searchWord)
    for i, word in enumerate(words):
      if word[:m] == searchWord:
        return i + 1
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("hello world", "wo"),
    ("hello world", "wow"),
  ]
  rslts = [solver.isPrefixOfWord(sentence, searchWord) for sentence, searchWord in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
