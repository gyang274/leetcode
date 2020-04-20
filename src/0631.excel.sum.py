from collections import defaultdict

class Excel:

  def __init__(self, H: int, W: str):
    self.cells = [[[0, defaultdict(lambda: 0), set([])] for _ in range(H)] for _ in range(ord(W) - ord("A") + 1)]

  def set(self, r: int, c: str, v: int) -> None:
    rr, cc = r - 1, ord(c) - ord("A")
    u = self.cells[rr][cc][0]
    self.cells[rr][cc][0] = v
    # if (rr, cc) should sum to some cells, update accordingly.
    if not v == u:
      for (sr, sc) in self.cells[rr][cc][1]:
        self.cells[sr][sc][0] += (v - u) * self.cells[rr][cc][1][(sr, sc)]
        # cascading propagation..
        
    # if (rr, cc) is sum of some cells, reset summation relationship.
    for ir, ic in self.cells[rr][cc][2]:
      self.cells[ir][ic][1].pop((rr, cc))
    self.cells[rr][cc][2] = set([])

  def get(self, r: int, c: str) -> int:
    return self.cells[r - 1][ord(c) - ord("A")][0]

  def sum(self, r: int, c: str, strs: List[str]) -> int:
    # sum cell row and col index
    rr, cc = r - 1, ord(c) - ord("A")
    # if (rr, cc) should sum to some cells, update accordingly. 
    u = self.cells[rr][cc][0]
    # if (rr, cc) is sum of some cells, reset summation relationship.
    for ir, ic in self.cells[rr][cc][2]:
      self.cells[ir][ic][1].pop((rr, cc))
    self.cells[rr][cc][2] = set([])
    # element cells
    self.cells[rr][cc][0] = 0
    for item in strs:
      item = item.split(":")
      if len(item) == 1:
        ar, ac = int(item[0][1:]) - 1, ord(item[0][0]) - ord("A")
        zr, zc = ar, ac
      else:
        ar, ac = int(item[0][1:]) - 1, ord(item[0][0]) - ord("A")
        zr, zc = int(item[1][1:]) - 1, ord(item[1][0]) - ord("A")
      for ir in range(ar, zr + 1):
        for ic in range(ac, zc + 1):
          # (ir, ic) => (rr, cc)
          self.cells[ir][ic][1][(rr, cc)] += 1
          # (rr, cc) <= (ir, ic)
          self.cells[rr][cc][0] += self.cells[ir][ic][0]
          self.cells[rr][cc][2].add((ir, ic))
    v = self.cells[rr][cc][0]
    for (sr, sc) in self.cells[rr][cc][1]:
      self.cells[sr][sc][0] += (v - u) * self.cells[rr][cc][1][(sr, sc)]
    print("sum", self.cells[rr][cc])
    return self.cells[rr][cc][0]

# ["Excel","get","set","get","sum","sum","get"]
# [[5,"E"],[1,"A"],[1,"A",1],[1,"A"],[2,"B",["A1","A1"]],[2,"B",["A1"]],[2,"B"]]

# ["Excel","get","set","get","sum","get","set","get","set","get","set","get","set","get"]
# [[3,"C"],[1,"A"],[1,"A",1],[1,"A"],[3,"C",["A1","A1:B2"]],[3,"C"],[1,"A",4],[3,"C"],[2,"B",3],[3,"C"],[3,"C",10],[3,"C"],[2,"B",2],[3,"C"]]

["Excel","set","set","set","sum","get","set","get","sum","set","get","get","sum","set","get","get","get","get"]
[[5,"E"],[1,"A",5],[1,"B",3],[1,"C",2],[1,"C",["A1","A1:B1"]],[1,"C"],[1,"B",5],[1,"C"],[1,"B",["A1:A5"]],[5,"A",10],[1,"B"],[1,"C"],[3,"C",["A1:C1","A1:A5"]],[3,"A",3],[1,"B"],[1,"C"],[3,"C"],[5,"A"]]
