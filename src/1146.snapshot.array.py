import bisect

class SnapshotArray:

  def __init__(self, length: int):
    # s: snapshot array
    self.s = [[[-1, 0]] for _ in range(length)]
    # i: snapshot id
    self.i = 0

  def set(self, index: int, val: int) -> None:
    x = self.s[index]
    if x and x[-1][0] == self.i:
      x[-1][1] = val
    else:
      x.append([self.i, val])

  def snap(self) -> int:
    self.i += 1
    return self.i - 1

  def get(self, index: int, snap_id: int) -> int:
    return self.s[index][bisect.bisect(self.s[index], [snap_id, float('inf')]) - 1][1]
