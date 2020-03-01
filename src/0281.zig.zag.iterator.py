from typing import List

class ZigzagIterator:
  """roll pull like network design.
  """
  def __init__(self, v1: List[int], v2: List[int]):
    # self.v
    self.v = [v1, v2]
    # self.k num of lists
    self.k = len(self.v)
    # self.j maintain the index of which list for next call
    self.j = 0
    # self.i maintain the index for next call within each list
    # direct extends to k lists, k = len(self.vs), vs: List[List[int]]
    self.i = [0] * self.k
    
  def next(self) -> int:
    if self.hasNext():
      x = self.v[self.j][self.i[self.j]]
      self.i[self.j] += 1
      self.j = (self.j + 1) % self.k
      return x
    # raise ValueError?
    return None

  def hasNext(self) -> bool:
    j = self.j
    while self.i[self.j] == len(self.v[self.j]):
      self.j = (self.j + 1) % self.k
      if self.j == j:
        return False
    return True

if __name__ == '__main__':
  cases = [
    ([], [1,2,3,4]),
    ([1], [2,3,4]),
    ([1,2], [3,4]),
    ([1,2,3], [4]),
    ([1,2,3,4], []),
  ]
  cases = [
    ZigzagIterator(v1, v2) for v1, v2 in cases
  ]
  rslts = []
  for cs in cases:
    rslt = []
    while cs.hasNext():
      rslt.append(cs.next())
    rslts.append(rslt)
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")