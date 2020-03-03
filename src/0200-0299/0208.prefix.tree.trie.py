class Trie:
  """prefix tree, applications in 0211 and 0212.
  """
  def __init__(self):
    """Initialize your data structure here.
    """
    self.prefix = {}
    self.value = None

  def insert(self, word: str) -> None:
    """Inserts a word into the trie.
    """
    node = self
    for x in word:
      if x not in node.prefix:
        node.prefix[x] = Trie()
      node = node.prefix[x]
    node.value = word
      
  def search(self, word: str) -> bool:
    """Returns if the word is in the trie.
    """
    node = self
    for x in word:
      if x in node.prefix:
        node = node.prefix[x]
      else:
        return False
    if node.value is None:
      return False
    return True

  def startsWith(self, prefix: str) -> bool:
    """Returns if there is any word in the trie that starts with the given prefix.
    """
    node = self
    for x in prefix:
      if x in node.prefix:
        node = node.prefix[x]
      else:
        return False
    return True

if __name__ == '__main__':
  trie = Trie()
  print(trie.insert("apple"))
  print(trie.search("apple"))   # returns true
  print(trie.search("app"))     # returns false
  print(trie.startsWith("app")) # returns true
  print(trie.insert("app"))
  print(trie.search("app"))     # returns true