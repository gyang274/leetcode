from collections import defaultdict

class FileSystem:

  def __init__(self):
    # constructor
    Trie = lambda: defaultdict(Trie)
    self.trie = Trie()
    # create the root path
    self.trie[''] = Trie()

  def createPath(self, path: str, value: int) -> bool:
    xs, node = path.split('/'), self.trie
    for x in xs[:-1]:
      if x not in node:
        return False
      node = node[x]
    if xs[-1] in node:
      return False
    node[xs[-1]]['#'] = value
    return True

  def get(self, path: str) -> int:
    xs, node = path.split('/'), self.trie
    for x in xs:
      if x not in node:
        return -1
      node = node[x]
    return node['#']

