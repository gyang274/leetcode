from typing import List
from collections import defaultdict
from functools import reduce

class Solution:
  
  def __init__(self, words: List[str]):
    # constructor
    Trie = lambda: defaultdict(Trie)
    # construct the trie of words
    self.trie = Trie()
    for word in words:
      reduce(dict.__getitem__, word, self.trie)['#'] = True
