class Node:
  def __init__(self, x):
    self.val = x
    self.children = []

class ThroneInheritance:

  def __init__(self, kingName: str):
    self.x = {kingName: Node(kingName)} 
    self.z = [kingName]
    self.r = False
    self.d = set()
    self.kingName = kingName

  def birth(self, parentName: str, childName: str) -> None:
    node = Node(childName)
    self.x[parentName].children.append(node)
    self.x[childName] = node      
    self.r = True

  def death(self, name: str) -> None:
    self.d.add(name)
    self.r = True
    return None

  def getInheritanceOrder(self) -> List[str]:
    if self.r:
      self.z = [self.kingName] if self.kingName not in self.d else []
      def recursive(name):
        for cnode in self.x[name].children:
          if cnode.val not in self.d:
            self.z.append(cnode.val)
          recursive(cnode.val)
      recursive(self.kingName)
      self.r = False
    return self.z
