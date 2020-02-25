class Solution:
  def __init__(self):
    self.strobo = [
      # strobo digit, rotated digit, number of strobo digits <= this, number of strobo digits >= this
      ("9", "6", 5),
      ("8", "8", 4),
      ("6", "9", 3),
      ("1", "1", 2),
      ("0", "0", 1),
    ]
    # as init, without 0
    self.stroboInit = [
      ("9", "6", 4),
      ("8", "8", 3),
      ("6", "9", 2),
      ("1", "1", 1),
    ]
    # as self, without 0
    self.stroboSelf = [
      ("8", 3),
      ("1", 2),
      ("0", 1),
    ]
    # memo: length k -> num strobogrammatic number
    self.memo = {
      0: 0,
      1: 3,
      2: 4,
    }
  def isStrobogrammatic(self, num: str) -> bool:
    """copy from Q0246.
    """
    strobo = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}
    i = 0
    for i in range((len(num) + 1) // 2):
      if not (num[i] in strobo and strobo[num[i]] == num[- (i + 1)]):
        return False
    return True
  def strobogrammaticLengthK(self, k):
    if k == 0:
      return 0
    elif k == 1:
      return 3
    else: # k > 1
      return 4 * (5 ** ((k - 2) // 2)) * (3 ** (k % 2))
  def strobogrammaticSameLengthLEStr(self, num, recursive=False, inclusive=True):
    """Args:
      recursive: whether or not func is called in recursive by itself or directly from outside.
        if direct from outside then `0` can be the 1st item (self.stroboInit), othersise in recursive ok (self.strobo).
    """
    k = len(num)
    if k == 0:
      return 0
    elif k == 1:
      for (s, n) in self.stroboSelf:
        if num >= s:
          return n if num > s or inclusive else n - 1
    else: # k > 1
      ans = 1
      strobo = self.stroboInit if not recursive else self.strobo
      for (s, r, n) in strobo:
        if num[0] >= s:
          if num[0] > s:
            ans = n * (5 ** ((k - 2) // 2)) * (3 ** (k % 2))
          # "889" -> (8, 9) and 8, so middle 8 gives (0, 1, 8), inclusive
          elif num[0] == s and num[-1] >= r:
            if k > 2:
              ans = (n - 1) * (5 ** ((k - 2) // 2)) * (3 ** (k % 2))
              ans += self.strobogrammaticSameLengthLEStr(num[1:-1], recursive=True, inclusive=True)
            else:
              ans = n
          # "886" -> (8, 6) and 8, so middle 8 gives (0, 1), exclusive
          else:
            # num[0] == s and num[-1] < r:
            if k > 2:  
              ans = (n - 1) * (5 ** ((k - 2) // 2)) * (3 ** (k % 2))
              ans += self.strobogrammaticSameLengthLEStr(num[1:-1], recursive=True, inclusive=False)
            else:
              ans = n - 1
          break
      else:
        return 0
      ans -= 1 if self.isStrobogrammatic(num) and not inclusive else 0
      return ans
  def strobogrammaticInRange(self, low: str, high: str) -> int:
    """Three functions:
      1. num of strobogrammatic number with length k.
      2. num of strobogrammatic number with same length and less than the low `str`.
      3. num of strobogrammatic number with same length and greater than high `str`.
      Note: 3 can be achieved by 1 and 2 and num itself is strobogrammatic or not as in Q0246.
    """
    kl, kh = len(low), len(high)
    # corner case
    if kl > kh or (kl == kh and low > high):
      return 0
    # main calculation
    ans = 0
    for k in range(kl, kh):
      ans += self.strobogrammaticLengthK(k)
    ans += self.strobogrammaticSameLengthLEStr(high)
    ans -= self.strobogrammaticSameLengthLEStr(low, inclusive=False)
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("0", "1"),
    ("42", "100"),
    ("687", "9695"),
    ("0", "9695"),
    ("0", "9697"),
    ("9695", "9697"),
    ("1101", "9679"),
    ("2358", "13213442"),
    ("0", "10695701"),
    ("0", "987110876"),
    ("10695701", "987110876"),
  ]
  rslts = [solver.strobogrammaticInRange(low, high) for low, high in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
