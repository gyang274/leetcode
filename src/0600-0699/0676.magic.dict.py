class MagicDictionary:

  def __init__(self):
    """Initialize your data structure here.
    """
    self.trie = {}

  def buildDict(self, dict: List[str]) -> None:
    """Build a dictionary through a list of words
    """
    for word in dict:
      node = self.trie
      for w in word:
        if w not in node:
          node[w] = {}
        node = node[w]
      node["#"] = 1
  
  def _searchExact(self, node, word):
    for w in word:
      if w not in node:
        return False
      else:
        node = node[w]
    return "#" in node
  
  def _searchWildCard(self, word, widx):
    node = self.trie
    for i, w in enumerate(word):
      if i == widx:
        for k in node:
          if not (k == w or k == "#") and self._searchExact(node[k], word[(i + 1):]):
            return True
      elif w in node:
        node = node[w]
      else:
        return False
    return False

  def search(self, word: str) -> bool:
    """Returns if there is any word in the trie that equals to the given word after modifying exactly one character
    """
    for i in range(len(word)):
      if self._searchWildCard(word, i):
        return True
    return False