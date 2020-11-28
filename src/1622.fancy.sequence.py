class Fancy:

  def __init__(self):
    # q: queue
    self.q = []
    # f: f[i] = T(m) * q[i] + S(a), fancy sequence..
    self.m = [1]
    self.a = [0]
    # M: module
    self.M = 10 ** 9 + 7

  def append(self, val: int) -> None:
    self.q.append(val)
    self.a.append(self.a[-1])
    self.m.append(self.m[-1])

  def addAll(self, inc: int) -> None:
    self.a[-1] += inc

  def multAll(self, m: int) -> None:
    self.m[-1] = (self.m[-1] * m) % self.M
    self.a[-1] = (self.a[-1] * m) % self.M
    
  def getIndex(self, idx: int) -> int:
    if idx >= len(self.q):
      return -1
    # Fermat's theorem: x^(M-1) = 1 (mod M), 
    # multiply both sides with x^(-1), x^(-1) = x^(M-2) (mod M).
    Tm = self.m[-1] * pow(self.m[idx], self.M - 2, self.M)
    Sa = self.a[-1] - self.a[idx] * Tm
    return (self.q[idx] * Tm + Sa) % self.M
