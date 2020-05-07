from typing import List
from itertools import zip_longest

class WordFilter:

  def __init__(self, words: List[str]):
    """prefix and suffix paired trie.
    """
    self.trie = {}
    for i, word in enumerate(words):
      node = self.trie
      node["#"] = i
      for k in range(len(word)):
        # prefix only
        hold = node
        for w in word[k:]:
          if (w, None) not in hold:
            hold[(w, None)] = {}
          hold = hold[(w, None)]
          hold["#"] = i
        # suffix only
        hold = node
        for w in word[:(len(word) - k)][::-1]:
          if (None, w) not in hold:
            hold[(None, w)] = {}
          hold = hold[(None, w)]
          hold["#"] = i
        # (prefix, suffix)
        if (word[k], word[~k]) not in node:
          node[(word[k], word[~k])] = {}
        node = node[(word[k], word[~k])]
        node["#"] = i
  def f(self, prefix: str, suffix: str) -> int:
    node = self.trie
    for u, v in zip_longest(prefix, suffix[::-1]):
      if (u, v) not in node:
        return -1
      node = node[(u, v)]
    return node["#"]

class WordFilter:

  def __init__(self, words: List[str]):
    """wrap around suffix to prefix, e.g., suffix^prefix into trie.
    """
    self.trie = {}
    for i, word in enumerate(words):
      node = self.trie
      node["#"] = i
      for k in range(len(word), -1, -1):
        wrap = word[k:] + '^' + word
        node = self.trie
        for w in wrap:
          if w not in node:
            node[w] = {}
          node = node[w]
          node["#"] = i
  def f(self, prefix: str, suffix: str) -> int:
    node = self.trie
    for w in suffix + '^' + prefix:
      if w not in node:
        return -1
      node = node[w]
    return node["#"]