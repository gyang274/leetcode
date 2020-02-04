from typing import List


class Solution:
  def justifySingleLine(self, words, length, maxWidth):
    """length: length of words connected with single space.
    """
    if len(words) == 1:
      return words[0] + ' ' * (maxWidth - length)
    else:
      # extra space
      es = maxWidth - length
      # extra space distributed
      s = [es // (len(words) - 1) for _ in range(len(words) - 1)]
      s = [1 + ds if i < es % (len(words) - 1) else ds for i, ds in enumerate(s)]
      return ' '.join([wi + ' ' * si for wi, si in zip(words, s + [0])])
  def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
    i, n, j, x, l = 1, len(words), 0, [[words[0], ], ], [len(words[0]), ]
    while i < n:
      if l[j] + 1 + len(words[i]) <= maxWidth:
        x[j].append(words[i])
        l[j] += 1 + len(words[i])
      else:
        j += 1
        x.append([words[i], ])
        l.append(len(words[i]))
      i += 1
    x = [self.justifySingleLine(ws, ls, maxWidth) for ws, ls in zip(x[:-1], l[:-1])] + [' '.join(x[-1]) + ' ' * (maxWidth - l[-1])]
    return x


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    (["This", "is", "an", "example", "of", "text", "justification."], 16),
    (["What","must","be","acknowledgment","shall","be"], 16),
    (["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20)
  ]
  rslts = [solver.fullJustify(words, maxWidth) for words, maxWidth in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")