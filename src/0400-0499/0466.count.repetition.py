class Solution:
  def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
    """Q0418, mapping s2 start index to search in s1 -> +counts,
      by pigeonhole principle, repetition must be found within len(s2) + 1 of s1.
    """
    # cs: character to start from s2 by searching along s1.
    # ds: dict cs -> (cs, count) next character to start, num of s2 completed.
    cs, ds = 0, {}
    while cs not in ds:
      ce, count = cs, 0
      for x in s1:
        if x == s2[ce]:
          ce += 1
          if ce == len(s2):
            ce = 0
            count += 1
      ds[cs] = (ce, count)
      cs = ce
    # brute force
    cs, count = 0, 0
    for i in range(n1):
      cs, icount = ds[cs]
      count += icount
    return count // n2

class Solution:
  def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
    """+ math to calculate through repetition.
    """
    # cs: character to start from s2 by searching along s1.
    # ds: dict cs -> (cs, count) next character to start, num of s2 completed.
    cs, ds = 0, {}
    while cs not in ds:
      ce, count = cs, 0
      for x in s1:
        if x == s2[ce]:
          ce += 1
          if ce == len(s2):
            ce = 0
            count += 1
      ds[cs] = (ce, count)
      cs = ce
    # track cs start index and count until repetition
    index, indexSet, count = [], set([]), []
    cs = 0
    for i in range(n1):
      if cs in indexSet:
        break
      index.append(cs)
      indexSet.add(cs)
      cs, icount = ds[cs]
      count.append(icount)
    # count (s2, n2) in (s1, n1)
    if cs not in indexSet:
      # no repetition yet.. n1 <= len(s2)
      m = sum(count) // n2
    else:
      i = index.index(cs)
      # print(f"{index=}, {count=}, {i=}")
      # sum(count[i:]) * ((n1 - i) // (len(count) - i)): num of s2 from repetition
      # sum(count[:(i + (n1 - i) % (len(count) - i))]): num of s2 from prev and next repeition (residuals)
      m = (sum(count[i:]) * ((n1 - i) // (len(count) - i)) + sum(count[:(i + (n1 - i) % (len(count) - i))])) // n2
    return m 

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("acb", 4, "ab", 2),
    ("cabcab", 123, "abc", 22),
    ("abaacdbac", 100, "adcbd", 4),
    ("aaa", 3, "aa", 1),
    ("ecbafedcba", 4, "abcdef", 1),
  ]
  rslts = [solver.getMaxRepetitions(s1, n1, s2, n2) for s1, n1, s2, n2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")