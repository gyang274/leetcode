class AutocompleteSystem:

  def __init__(self, sentences: List[str], times: List[int]):
    self.root = self._createTrie(sentences, times)
    self.node = self.root
    self.prefix = ""

  def _createTrie(self, sentences, times):
    root = {}
    for sentence, time in zip(sentences, times):
      node = root
      for x in sentence:
        if x not in node:
          node[x] = {}
        node = node[x]
      node["#"] = time
    return root
  
  def _getSuffix(self, node):
    suffix = []
    for child in node:
      if child == "#":
        suffix.append((-node[child], ""))
      else:
        for csuffix in self._getSuffix(node[child]):
          suffix.append((csuffix[0], child + csuffix[1]))
    suffix.sort()
    return suffix[:3]

  def input(self, c: str) -> List[str]:
    if c not in self.node:
      if c == "#":
        self.node[c] = 1
        self.node = self.root
        self.prefix = ""
      else:
        self.node[c] = {}
        self.node = self.node[c]
        self.prefix += c
      return []
    elif c == "#":
      self.node[c] += 1
      self.node = self.root
      self.prefix = ""
      return []
    else:
      self.node = self.node[c]
      self.prefix += c
      return [self.prefix + suffix[1] for suffix in self._getSuffix(self.node)]
