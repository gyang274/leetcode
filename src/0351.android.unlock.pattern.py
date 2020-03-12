class Solution:
  def __init__(self):
    self.candidates = {
      1: {
        # next: keys with when value > 0 can be the next
        'next': {
          1: 0,
          2: 1,
          3: 0,
          4: 1,
          5: 1,
          6: 1,
          7: 0,
          8: 1,
          9: 0,
        },
        # lock: if 2 is hitted then 3 can be next, e.g., value as key in next which's value +1 in next
        'lock': {
          2: 3,
          4: 7,
          5: 9,
        }
      },
      2: {
        'next': {
          1: 1,
          2: 0,
          3: 1,
          4: 1,
          5: 1,
          6: 1,
          7: 1,
          8: 0,
          9: 1,
        },
        'lock': {
          5: 8
        }
      },
      3: {
        'next': {
          1: 0,
          2: 1,
          3: 0,
          4: 1,
          5: 1,
          6: 1,
          7: 0,
          8: 1,
          9: 0,
        },
        'lock': {
          2: 1,
          5: 7,
          6: 9,
        }
      },
      4: {
        'next': {
          1: 1,
          2: 1,
          3: 1,
          4: 0,
          5: 1,
          6: 0,
          7: 1,
          8: 1,
          9: 1,
        },
        'lock': {
          5: 6
        }
      },
      5: {
        'next': {
          1: 1,
          2: 1,
          3: 1,
          4: 1,
          5: 1,
          6: 1,
          7: 1,
          8: 1,
          9: 9,
        },
        'lock': {}
      },
      6: {
        'next': {
          1: 1,
          2: 1,
          3: 1,
          4: 0,
          5: 1,
          6: 0,
          7: 1,
          8: 1,
          9: 1,
        },
        'lock': {
          5: 4
        }
      },
      7: {
        'next': {
          1: 0,
          2: 1,
          3: 0,
          4: 1,
          5: 1,
          6: 1,
          7: 0,
          8: 1,
          9: 0,
        },
        'lock': {
          4: 1,
          5: 3,
          8: 9,
        }
      },
      8: {
        'next': {
          1: 1,
          2: 0,
          3: 1,
          4: 1,
          5: 1,
          6: 1,
          7: 1,
          8: 0,
          9: 1,
        },
        'lock': {
          5: 2
        }
      },
      9: {
        'next': {
          1: 0,
          2: 1,
          3: 0,
          4: 1,
          5: 1,
          6: 1,
          7: 0,
          8: 1,
          9: 0,
        },
        'lock': {
          5: 1,
          6: 3,
          8: 7,
        }
      }
    }
  def _locked(self, x):
    for i in self.candidates:
      if x in self.candidates[i]['lock']:
        self.candidates[i]['next'][self.candidates[i]['lock'][x]] -= 1
  def _unlock(self, x):
    for i in self.candidates:
      if x in self.candidates[i]['lock']:
        self.candidates[i]['next'][self.candidates[i]['lock'][x]] += 1
  def recursive(self, path):
    if len(path) >= self.m:
      # self.ans.append(path.copy())
      self.counter += 1
    if len(path) >= self.n:
      return None
    if len(path) == 0:
      candidates = [1,2,3,4,5,6,7,8,9]
    else:
      candidates = [x for x in self.candidates[path[-1]]['next'] if self.candidates[path[-1]]['next'][x] > 0]
    # print(f"{path=}, {candidates=}")
    for i in candidates:
      if i not in path:
        # hit i, released next locked by i
        self._unlock(i)
        # recusrive over path
        self.recursive(path + [i])
        # reset candidate for next recursive call
        self._locked(i)
    return None
  def numberOfPatterns(self, m: int, n: int) -> int:
    self.m, self.n = m, n
    # self.ans = []
    self.counter = 0
    self.recursive([])
    return self.counter

class Solution:
  def __init__(self):
    self.candidates = {
      1: {
        # next: keys with when value > 0 can be the next
        'next': {
          1: 0,
          2: 1,
          3: 0,
          4: 1,
          5: 1,
          6: 1,
          7: 0,
          8: 1,
          9: 0,
        },
        # lock: if 2 is hitted then 3 can be next, e.g., value as key in next which's value +1 in next
        'lock': {
          2: 3,
          4: 7,
          5: 9,
        }
      },
      2: {
        'next': {
          1: 1,
          2: 0,
          3: 1,
          4: 1,
          5: 1,
          6: 1,
          7: 1,
          8: 0,
          9: 1,
        },
        'lock': {
          5: 8
        }
      },
      3: {
        'next': {
          1: 0,
          2: 1,
          3: 0,
          4: 1,
          5: 1,
          6: 1,
          7: 0,
          8: 1,
          9: 0,
        },
        'lock': {
          2: 1,
          5: 7,
          6: 9,
        }
      },
      4: {
        'next': {
          1: 1,
          2: 1,
          3: 1,
          4: 0,
          5: 1,
          6: 0,
          7: 1,
          8: 1,
          9: 1,
        },
        'lock': {
          5: 6
        }
      },
      5: {
        'next': {
          1: 1,
          2: 1,
          3: 1,
          4: 1,
          5: 1,
          6: 1,
          7: 1,
          8: 1,
          9: 9,
        },
        'lock': {}
      },
      6: {
        'next': {
          1: 1,
          2: 1,
          3: 1,
          4: 0,
          5: 1,
          6: 0,
          7: 1,
          8: 1,
          9: 1,
        },
        'lock': {
          5: 4
        }
      },
      7: {
        'next': {
          1: 0,
          2: 1,
          3: 0,
          4: 1,
          5: 1,
          6: 1,
          7: 0,
          8: 1,
          9: 0,
        },
        'lock': {
          4: 1,
          5: 3,
          8: 9,
        }
      },
      8: {
        'next': {
          1: 1,
          2: 0,
          3: 1,
          4: 1,
          5: 1,
          6: 1,
          7: 1,
          8: 0,
          9: 1,
        },
        'lock': {
          5: 2
        }
      },
      9: {
        'next': {
          1: 0,
          2: 1,
          3: 0,
          4: 1,
          5: 1,
          6: 1,
          7: 0,
          8: 1,
          9: 0,
        },
        'lock': {
          5: 1,
          6: 3,
          8: 7,
        }
      }
    }
  def _locked(self, x):
    for i in self.candidates:
      if x in self.candidates[i]['lock']:
        self.candidates[i]['next'][self.candidates[i]['lock'][x]] -= 1
  def _unlock(self, x):
    for i in self.candidates:
      if x in self.candidates[i]['lock']:
        self.candidates[i]['next'][self.candidates[i]['lock'][x]] += 1
  def recursive(self, path):
    if len(path) >= self.m:
      self.counter += 1 if path[0] == 5 else 4
    if len(path) >= self.n:
      return None
    if len(path) == 0:
      candidates = [1,2,5]
    else:
      candidates = [x for x in self.candidates[path[-1]]['next'] if self.candidates[path[-1]]['next'][x] > 0]
    # print(f"{path=}, {candidates=}")
    for i in candidates:
      if i not in path:
        # hit i, released next locked by i
        self._unlock(i)
        # recusrive over path
        self.recursive(path + [i])
        # reset candidate for next recursive call
        self._locked(i)
    return None
  def numberOfPatterns(self, m: int, n: int) -> int:
    self.m, self.n = m, n
    self.counter = 0
    self.recursive([])
    return self.counter

class Solution:
  def __init__(self):
    self.seen = set([])
  # def isValid(self, i: int, j: int) -> bool:
  #   # isValid to hit j after i?
  #   if j in self.seen:
  #     return False
  #   # 1st of the pattern
  #   if i == -1:
  #     return True
  #   # knight moves or adjacent cells (in a row or in a column)
  #   if ((i + j) % 2 == 1):
  #     return True
  #   # indexes are at both end of the diagonals for example 1 and 9
  #   m = (i + j) // 2
  #   if m == 5:
  #     return m in self.seen
  #   # adjacent cells on diagonal - for example 1 and 5
  #   if (((i-1)%3 != (j-1)%3) & ((i-1)//3 != (j-1)//3)):
  #     return True
  #   # all other cells which are not adjacent
  #   return m in self.seen
  def isValid(self, i: int, j: int) -> bool:
    # isValid i -> j? 
    if j in self.seen:
      return False
    # 1st in pattern
    if i == -1:
      return True
    # center, edge, corner
    if i == 5:
      return True
    elif i in {2, 4, 6, 8}:
      if 5 in self.seen:
        return True
      elif not i + j == 10:
        return True
      else:
        return False
    elif i in {1, 3, 7, 9}:
      if j in {2, 4, 5, 6, 8}:
        return True
      # note: j also in 1, 3, 7, 9 and not i == j
      elif (i + j) // 2 in self.seen:
        return True
      else:
        return False
    return False
  def recursive(self, path):
    if len(path) > self.m:
      self.counter += 1
    if len(path) > self.n:
      return None
    for i in [1,2,3,4,5,6,7,8,9]:
      if i not in self.seen and self.isValid(path[-1], i):
        self.seen.add(i)
        self.recursive(path + [i])
        self.seen.remove(i)
  def numberOfPatterns(self, m: int, n: int) -> int:
    self.m, self.n = m, n
    self.counter = 0
    self.recursive([-1])
    return self.counter

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 9),
  ]
  rslts = [solver.numberOfPatterns(m, n) for m, n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")