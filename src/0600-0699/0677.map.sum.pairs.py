class MapSum:

  def __init__(self):
    """Initialize your data structure here.
    """
    self.trie = {}

  def insert(self, key: str, val: int) -> None:
    node, stack = self.trie, []
    stack.append(node)
    for w in key:
      if w not in node:
        node[w] = {}
      node = node[w]
      stack.append(node)
    preVal = node["#"] if "#" in node else 0
    node["#"] = val
    for node in stack:
      node["*"] = (node["*"] + val - preVal) if "*" in node else (val - preVal)

  def sum(self, prefix: str) -> int:
    node = self.trie
    for w in prefix:
      if w in node:
        node = node[w]
      else:
        return 0
    return node["*"]