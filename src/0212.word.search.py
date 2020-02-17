from typing import List
from collections import defaultdict

# Solution: version1
class Trie:
  """prefix tree, applications in 0211 and 0212.
  """
  def __init__(self):
    """Initialize trie data structure.
    """
    # init trie
    self.prefix = defaultdict(Trie)

  def create(self, board: List[List[str]]) -> None:
    """construct the trie for a given board.
    """
    self.board = board
    # contruct trie for a given board
    self.n = len(self.board)
    if self.n == 0:
      return None
    self.m = len(self.board[0])
    if self.m == 0:
      return None
    self.d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for i in range(self.n):
      for j in range(self.m):
        self._create_from_node(self, i, j)

  def _create_from_node(self, node, i, j):
    x = self.board[i][j]
    node = node.prefix[x]
    self.board[i][j] = '#'
    for di, dj in self.d:
      pi, pj = i + di, j + dj
      if 0 <= pi < self.n and 0 <= pj < self.m and not self.board[pi][pj] == '#':
        self._create_from_node(node, pi, pj)
    self.board[i][j] = x

  def search(self, word: str) -> bool:
    """Returns if the word is in the trie.
    """
    node = self
    for x in word:
      if x in node.prefix:
        node = node.prefix[x]
      else:
        return False
    return True

class Solution:
  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    """Key: 0079 and 0208.
      0208 construct prefix tree once, and search multiple times, or same as 0079 dfs when search once.
    """
    trie = Trie()
    trie.create(board)
    return [w for w in words if trie.search(w)]

# Solution: version2
class Trie:
  """prefix tree, applications in 0211 and 0212.
  """
  def __init__(self):
    """Initialize trie data structure.
    """
    # init trie
    self.prefix = defaultdict(Trie)

  def create(self, board: List[List[str]], k: int) -> None:
    """construct the trie for a given board.
      improvement: construct the prefix for entire board is time consuming as prefix can go very deep to level n * m,
        so, limit the level to k, where k = max(len(words)).
    """
    self.board, self.k = board, k
    # contruct trie for a given board
    self.n = len(self.board)
    if self.n == 0:
      return None
    self.m = len(self.board[0])
    if self.m == 0:
      return None
    self.d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for i in range(self.n):
      for j in range(self.m):
        self._create_from_node(self, i, j, 0)

  def _create_from_node(self, node, i, j, k):
    x = self.board[i][j]
    node = node.prefix[x]
    if k < self.k:
      self.board[i][j] = '#'
      for di, dj in self.d:
        pi, pj = i + di, j + dj
        if 0 <= pi < self.n and 0 <= pj < self.m and not self.board[pi][pj] == '#':
          self._create_from_node(node, pi, pj, k + 1)
      self.board[i][j] = x

  def search(self, word: str) -> bool:
    """Returns if the word is in the trie.
    """
    node = self
    for x in word:
      if x in node.prefix:
        node = node.prefix[x]
      else:
        return False
    return True

class Solution:
  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    """Key: 0079 and 0208.
      0208 construct prefix tree once, and search multiple times, or same as 0079 dfs when search once.
    """
    if len(words) == 0:
      return []
    k = max([len(w) for w in words])
    trie = Trie()
    trie.create(board, k)
    return [w for w in words if trie.search(w)]

# Solution: version3
#   build Trie() around words instead of board.
class Trie:
  """prefix tree, applications in 0211 and 0212 - copy from 0208.
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

  def startsWithStrict(self, prefix: str) -> bool:
    """Returns if there is any word in the trie that starts with the given prefix.
    """
    node = self
    for x in prefix:
      if x in node.prefix:
        node = node.prefix[x]
      else:
        return False
    # modified: `strict` startsWith, must have pending characters.
    if not node.prefix:
      return False
    return True

class Solution:
  def backtrack(self, prefix, i, j):
    x = self.board[i][j]
    self.board[i][j] = '#'
    prefix += x
    if self.trie.search(prefix):
      self.ans.add(prefix)
      # prune the Trie()?
    if self.trie.startsWithStrict(prefix):
      for di, dj in self.d:
        pi, pj = i + di, j + dj
        if 0 <= pi < self.n and 0 <= pj < self.m and not self.board[pi][pj] == '#':
          self.backtrack(prefix, pi, pj)
    self.board[i][j] = x
  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    # board
    self.board = board
    self.n = len(self.board)
    if self.n == 0:
      return []
    self.m = len(self.board[0])
    if self.m == 0:
      return []
    self.d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # words
    self.words = set(words)
    if (len(self.words)) == 0:
      return []
    self.trie = Trie()
    for word in self.words:
      self.trie.insert(word)
    # ans
    self.ans = set([])
    for i in range(self.n):
      for j in range(self.m):
        self.backtrack("", i, j)
    return self.ans

# Solution: verion4
#   simplified Trie(), move node along with board so less comparison for checking prefix startsWith()
class Trie:
  def __init__(self):
    self.prefix = defaultdict(Trie)
    self.value = None

class Solution:
  def backtrack(self, prefix, i, j, parent):
    x = self.board[i][j]
    if x in parent.prefix:
      prefix += x
      node = parent.prefix[x]
      # prefix is a word matches word from words
      if node.value == prefix:
        self.ans.add(prefix)
        if not node.prefix:
          # leaf node, prune the Trie(), mitigate duplicated (re)matrch
          _ = parent.prefix.pop(x)
      # recursvie move forward follow the path
      if node.prefix:
        self.board[i][j] = '#'
        for di, dj in self.d:
          pi, pj = i + di, j + dj
          if 0 <= pi < self.n and 0 <= pj < self.m and not self.board[pi][pj] == '#':
            self.backtrack(prefix, pi, pj, node)
        self.board[i][j] = x
  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    # simplified Trie()
    self.trie = Trie()
    for word in words:
      node = self.trie
      for x in word:
        node = node.prefix[x]
      node.value = word
    # backtrack over board
    self.board = board
    self.n, self.m, self.d = len(board), len(board[0]), [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # backtrack essentials
    self.ans = set([])
    for i in range(self.n):
      for j in range(self.m):
        self.backtrack("", i, j, self.trie)
    return self.ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (
      [
        ["a"]
      ], ["a"]
    ),
    (
      [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
      ], ["oath","pea","eat","rain"]
    ),
    (
      [
        ["b","b","a","a","b","a"],
        ["b","b","a","b","a","a"],
        ["b","b","b","b","b","b"],
        ["a","a","a","b","a","a"],
        ["a","b","a","a","b","b"]
      ], ["abbbababaa"]
    ),
    (
      [
        ["b","a","a","b","a","b"],
        ["a","b","a","a","a","a"],
        ["a","b","a","a","a","b"],
        ["a","b","a","b","b","a"],
        ["a","a","b","b","a","b"],
        ["a","a","b","b","b","a"],
        ["a","a","b","a","a","b"]
      ], [
        "bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa",
        "bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa",
        "babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa",
        "aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab",
        "aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa",
        "aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb",
        "aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab",
        "bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab",
        "aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa",
        "abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa",
      ]
    ),
  ]
  rslts = [solver.findWords(board, words) for board, words in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")