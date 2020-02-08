import copy


class Solution:
  def minWindow(self, s: str, t: str) -> str:
    """dynamic programming
    """
    if t == "":
      return ""
    u, n = {}, len(s)
    for x in set(t):
      xs = s.count(x)
      xt = t.count(x)
      if xs >= xt:
        u[x] = [xs, xt]
      else:
        return ""
    memo = {}
    def dp(s, t, u, i, j):
      if (i, j) in memo:
        return memo[(i, j)]
      else:
        ki, kj = i, j
        while s[i] not in t:
          i += 1
        while s[j] not in t:
          j -= 1
        if u[s[i]][0] > u[s[i]][1] and u[s[j]][0] > u[s[j]][1]:
          uCopy0 = copy.deepcopy(u)
          uCopy0[s[i]][0] -= 1
          i0, j0 = dp(s, t, uCopy0, i + 1, j)
          uCopy1 = copy.deepcopy(u)
          uCopy1[s[j]][0] -= 1
          i1, j1 = dp(s, t, uCopy1, i, j - 1)
          i, j = (i0, j0) if (j0 - i0) <= (j1 - i1) else (i1, j1)
        elif u[s[i]][0] > u[s[i]][1]:
          uCopy0 = copy.deepcopy(u)
          uCopy0[s[i]][0] -= 1
          i, j = dp(s, t, uCopy0, i + 1, j)
        elif u[s[j]][0] > u[s[j]][1]:
          uCopy1 = copy.deepcopy(u)
          uCopy1[s[j]][0] -= 1
          i, j = dp(s, t, uCopy1, i, j - 1)
        memo[(ki, kj)] = (i, j)
        return (i, j)
    l, r = dp(s, t, u, 0, n - 1)
    return s[l:(r + 1)]


class Solution:
  def minWindow(self, s: str, t: str) -> str:
    """Two pointers + drag and chase slide.
    """
    if t == "":
      return ""
    u, v = {}, [False for _ in range(len(set(t)))]
    for i, x in enumerate(set(t)):
      # char x: count of current covered: xc, count in t: xt, index in covered or not list: v
      u[x] = [0, t.count(x), i]
    n = len(s)
    l, minL = 0, 0
    r, minR = 0, 0
    k, minK = n + 1, n + 1
    # repeat:
    #   move right (drag) until t is covered
    #   move left (chase) until t is just uncovered
    # until
    #   no enough unvisited to recover t
    def moveRight(r):
      while not all(v) and r < n:
        x = s[r]
        if x in t:
          u[x][0] += 1
          v[u[x][2]] = (u[x][0] >= u[x][1])
        r += 1
      return r
    def moveLeft(l):
      while all(v) and l < n:
        x = s[l]
        if x in t:
          u[x][0] -= 1
          v[u[x][2]] = (u[x][0] >= u[x][1])
        l += 1
      return l
    while l < n and r < n:
      r = moveRight(r)
      if all(v):
        l = moveLeft(l)
        k = r - l + 1
        if k < minK:
          minK, minL, minR = k, l, r
      else:
        break
    return "" if minK == n + 1 else s[(minL - 1):minR]


class Solution:
  def minWindow(self, s: str, t: str) -> str:
    """Two pointers + drag and chase slide.
      Improvement:
        1. preprocess filter S out of positions of characters in T, works when |filteredS| <<< |S|
        2. early stop
    """
    if t == "":
      return ""
    u, v, w = {}, [False for _ in range(len(set(t)))], []
    # preprocess t
    for i, x in enumerate(set(t)):
      # char x: count in t: xt, count of current covered: xc, count of unvisited: xu, index in covered or not list: v
      u[x] = [t.count(x), 0, 0, i]
    # preprocess s
    for i, x in enumerate(s):
      if x in u:
        w.append((i, x))
        u[x][2] += 1
    # early stop 1
    for x, (xt, xc, xu, xv) in u.items():
      if xu < xt:
        return ""
    # print(f"{u=}, {v=}, {w=}")
    # main
    n = len(w)
    l, minL = 0, 0
    r, minR = 0, 0
    k, minK = len(s) + 1, len(s) + 1
    # repeat:
    #   move right (drag) until t is covered
    #   move left (chase) until t is just uncovered
    # until
    #   no enough unvisited to recover t
    def moveRight(r):
      while not all(v) and r < n:
        x = w[r][1]
        u[x][1] += 1
        u[x][2] -= 1
        v[u[x][3]] = (u[x][1] >= u[x][0])
        r += 1
      return r
    def moveLeft(l):
      while all(v) and l < n:
        x = w[l][1]
        u[x][1] -= 1
        v[u[x][3]] = (u[x][1] >= u[x][0])
        l += 1
      return l, x
    while l < n and r < n:
      r = moveRight(r)
      if all(v):
        l, x = moveLeft(l)
        k = w[r - 1][0] - w[l - 1][0] + 1
        if k < minK:
          minK, minL, minR = k, w[l - 1][0], w[r - 1][0]
        # early stop 2:
        #  no more x for recover again
        if u[x][2] == 0:
          break
      else:
        break
    return "" if minK == len(s) + 1 else s[minL:(minR + 1)]


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    # ("A", "A"),
    # ("BBA", "AB"),
    ("ABC", "AC"),
    # ("ADOBECODEBANC", "ABC"),
    # ("ADOBECODEBANC", "AABC"),
    # ("ask_not_what_your_country_can_do_for_you_ask_what_you_can_do_for_your_country", "ask_country"),
    # ("xeaifhaqslynbcwxncwgeezbrjorzyuwevejcecuscjvgfutkrcqxbromihlgcjnzpybwcxqeglknhgzyiqxljnyrvlazvnyklbgoywugjftrltrvlrgueeobsoandazqbigbgbhqgdjtycojtwfydtbvjekmejdirjlymvquybnyddjxaoxfkyatckijvlrnwcnjxfdxgtvjweiyvfdhefaipkrnviaunpfmukkcdhlcmwcjbgqhnsqfdhsasuwhjbtfmdhrluvzqykugcbtutyzdqcxkyevaxcodjhogdpwbzsjducxpdzsvbpizvfbtirwtzmzebyhcqqfmueczdwveofgjkhesbamaolgrlpvcfcqbhubmtythdzspizijbwlqjrjvgfznhprqmudfsyoxzimhhutjsebcykxgpywznnpbhuizuwythkbohwzzacbanyhewdfmsvpzryamuyhdkkurgvrjysjntqrrvxfnuvonvqbrqjvbvpucklligu", "xbnpukocakzqzuhdlxoga"),
  ]
  rslts = [solver.minWindow(s, t) for s, t in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")