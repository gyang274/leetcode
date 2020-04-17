class FileSystem:

  def __init__(self):
    self.d = {}

  def ls(self, path: str) -> List[str]:
    d = self.d
    if not path == "/":
      path = path[1:].split("/")
      for k in path:
        d = d[k]
    return sorted(d.keys()) if isinstance(d, dict) else [path[-1]]

  def mkdir(self, path: str) -> None:
    d = self.d
    path = path[1:].split("/")
    for k in path:
      if k not in d:
        d[k] = {}
      d = d[k]
    return None

  def addContentToFile(self, filePath: str, content: str) -> None:
    d = self.d
    path = filePath[1:].split("/")
    for k in path[:-1]:
      if k not in d:
        d[k] = {}
      d = d[k]
    if path[-1] not in d:
      d[path[-1]] = ""
    d[path[-1]] += content
    return None

  def readContentFromFile(self, filePath: str) -> str:
    d = self.d
    path = filePath[1:].split("/")
    for k in path[:-1]:
      if k not in d:
        d[k] = {}
      d = d[k]          
    return d[path[-1]]

