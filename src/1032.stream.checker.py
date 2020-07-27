from collections import defaultdict
from functools import reduce

class StreamChecker:

  def __init__(self, words: List[str]):
    # trie of words
    self.trie = {}
    for word in words:
      node = self.trie
      for x in word:
        if x not in node:
          node[x] = {}
        node = node[x]
      node['#'] = 1
    # nodes pending to query
    self.qnodes = []

  def query(self, letter: str) -> bool:
    x, ok = letter, False
    qnuxts = []
    for node in self.qnodes + [self.trie]:
      if x in node:
        node = node[x]
        if '#' in node:
          ok = True
          if len(node) > 1:
            qnuxts.append(node)
        else:
          qnuxts.append(node)
    self.qnodes = qnuxts
    return ok

class StreamChecker:

  def __init__(self, words: List[str]):
    T = lambda: defaultdict(T)
    self.trie = T()
    for w in words: reduce(dict.__getitem__, w, self.trie)['#'] = True
    self.waiting = []

  def query(self, letter: str) -> bool:
    self.waiting = [node[letter] for node in self.waiting + [self.trie] if letter in node]
    return any("#" in node for node in self.waiting)

class StreamChecker:

  def __init__(self, words: List[str]):
    # build the trie of reverse words
    T = lambda: defaultdict(T)
    self.trie = T()
    for w in words: reduce(dict.__getitem__, w[::-1], self.trie)['#'] = True
    self.s = ''
    self.L = max(map(len, words))

  def query(self, letter: str) -> bool:
    # query directly
    self.s = (letter + self.s)[:self.L]
    node = self.trie
    for x in self.s:
      if x in node:
        node = node[x]
        if '#' in node:
          return True
      else:
        break
    return False