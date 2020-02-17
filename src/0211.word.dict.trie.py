class WordDictionary:
  def __init__(self):
    """Initialize your data structure here.
    """
    self.prefix = {}
    self.value = None
    
  def addWord(self, word: str) -> None:
    """Adds a word into the data structure.
    """
    node = self
    for x in word:
      if x not in node.prefix:
        node.prefix[x] = WordDictionary()
      node = node.prefix[x]
    node.value = word

  def search(self, word: str) -> bool:
    """Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
    """
    return self._search_from_node(self, word)

  def _search_from_node(self, node, word: str) -> bool:
    for i, x in enumerate(word):
      if x == '.':
        for z in node.prefix:
          if self._search_from_node(node.prefix[z], word[(i + 1):]):
            return True
        else:
          return False
      elif x in node.prefix:
        node = node.prefix[x]
      else:
        return False
    if node.value is None:
      return False
    return True

if __name__ == '__main__':
  wd = WordDictionary()
  print(wd.addWord("bad"))
  print(wd.addWord("dad"))
  print(wd.addWord("mad"))
  print(wd.search("pad"))  #-> false
  print(wd.search("bad"))  #-> true
  print(wd.search(".ad"))  #-> true
  print(wd.search("b.."))  #-> true
  print(wd.search("b."))   #-> false