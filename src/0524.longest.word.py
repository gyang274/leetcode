from typing import List

class Solution:
  def findLongestWord(self, s: str, d: List[str]) -> str:
    """O(N + L): N: num character in s, L: total num of character of all words in d.
      https://techdevguide.withgoogle.com/paths/foundational/find-longest-word-in-dictionary-that-subsequence-of-given-string/#
      Aho-Corasick Algorithm: https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm
    """
    return NotImplemented

class Solution:
  def insertTrie(self, x, node) -> None:
    # insert x (character) into every node of trie, recursively.
    for k in node:
      self.insertTrie(x, node[k])
    if x not in node:
      node[x] = {}
    return None
  def detectTrie(self, s, node) -> bool:
    # construct s (str) by traverse trie?
    for x in s:
      if x not in node:
        return False
      node = node[x]
    return True
  def findLongestWord(self, s: str, d: List[str]) -> str:
    # trie
    trie = {}
    for x in s:
      self.insertTrie(x, trie)
    # dict
    d.sort(key=lambda x: (-len(x), x))
    for t in d:
      if self.detectTrie(t, trie):
        return t
    return ""

class Solution:
  def construct(self, s, t):
    i, j = 0, 0
    while j < len(t):
      while i < len(s) and not s[i] == t[j]:
        i += 1
      if i == len(s):
        return False
      i += 1
      j += 1
    return True
  def findLongestWord(self, s: str, d: List[str]) -> str:
    """O(N*W), N: num character in s, W: num of words in d.
    """
    d.sort(key=lambda x: (-len(x), x))
    for t in d:
      if self.construct(s, t):
        return t
    return ""

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("abpcplea", ["a","b","c"]),
    ("abpcplea", ["ale","apple","monkey","plea"]),
    ("aewfafwafjlwajflwajflwafj", ["apple","ewaf","awefawfwaf","awef","awefe","ewafeffewafewf"]),
  ]
  rslts = [solver.findLongestWord(s, d) for s, d in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
