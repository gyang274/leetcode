import bisect

class RangeModule:

  def __init__(self):
    self.ranges = []

  def addRange(self, left: int, right: int) -> None:
    # print(f"add [{left}, {right}) into {self.ranges}")
    l = bisect.bisect_left(self.ranges, left)
    r = bisect.bisect_right(self.ranges, right)
    if l & 1:
      if r & 1:
        self.ranges = self.ranges[:l] + self.ranges[r:]
      else:
        self.ranges = self.ranges[:l] + [right] + self.ranges[r:]
    else:
      if r & 1:
        self.ranges = self.ranges[:l] + [left] + self.ranges[r:]
      else:
        self.ranges = self.ranges[:l] + [left, right] + self.ranges[r:]
    # print(f"->> {self.ranges}")
    return None

  def queryRange(self, left: int, right: int) -> bool:
    l = bisect.bisect_left(self.ranges, left)
    r = bisect.bisect_right(self.ranges, right)
    # print(f"query, [{left}, {right}), {l, r}")
    if l == len(self.ranges) or r == 0:
      return False
    if l & 1 == 0 and self.ranges[l] == left:
      l += 1
    if r & 1 == 0 and self.ranges[r - 1] == right:
      r -= 1
    # print(f"query, [{left}, {right}), {l, r}")
    return l & 1 and l == r

  def removeRange(self, left: int, right: int) -> None:
    # print(f"del [{left}, {right}) from {self.ranges}")
    l = bisect.bisect_left(self.ranges, left)
    r = bisect.bisect_right(self.ranges, right)
    if l & 1:
      if r & 1:
        self.ranges = self.ranges[:l] + [left, right] + self.ranges[r:]
      else:
        self.ranges = self.ranges[:l] + [left] + self.ranges[r:]
    else:
      if r & 1:
        self.ranges = self.ranges[:l] + [right] + self.ranges[r:]
      else:
        self.ranges = self.ranges[:l] + self.ranges[r:]
    # print(f"->> {self.ranges}")
    return None

if __name__ == '__main__':
  rangeModule = RangeModule()
  actions = ["RangeModule","addRange","removeRange","queryRange","queryRange","queryRange"]
  params = [[],[10,20],[14,16],[10,14],[13,15],[16,17]]
  for action, param in zip(actions[1:], params[1:]):
    if action == "addRange":
      rangeModule.addRange(*param)
    elif action == "removeRange":
      rangeModule.removeRange(*param)
    elif action == "queryRange":
      rangeModule.queryRange(*param)
    else:
      print('Error: invalid action.')
