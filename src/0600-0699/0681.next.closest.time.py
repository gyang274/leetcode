import itertools

class Solution:
  def _elapsed(self, t0, t1):
    h0, m0 = [int(x) for x in t0.split(":")]
    h1, m1 = [int(x) for x in t1.split(":")]
    return ((h1 * 60 + m1) - (h0 * 60 + m0)) % 1440
  def nextClosestTime(self, time: str) -> str:
    s = set(time) - {":"}
    hh = ["".join(z) for z in itertools.product(s, repeat=2) if "".join(z) < "24"]
    mm = ["".join(z) for z in itertools.product(s, repeat=2) if "".join(z) < "60"]
    d, t = 1440, time
    for h1 in hh:
      for m1 in mm:
        t1 = h1 + ":" + m1
        if not t1 == time:
          d1 = self._elapsed(time, t1)
          if d1 < d:
            d, t = d1, t1
    return t

class Solution:
  def nextClosestTime(self, time: str) -> str:
    # time2int
    h0, m0 = [int(x) for x in time.split(":")]
    t0 = h0 * 60 + m0
    # brute-force up to 256 candidates
    s = {int(x) for x in set(time) - {":"}}
    d1, h1, m1 = 1440, h0, m0
    for hhd1, hhd0, mmd1, mmd0 in itertools.product(s, repeat=4):
      hh, mm = hhd1 * 10 + hhd0, mmd1 * 10 + mmd0
      if hh < 24 and mm < 60:
        tt = hh * 60 + mm
        if not tt == t0:
          dd = (tt - t0) % 1440
          if dd < d1:
            d1, h1, m1 = dd, hh, mm
    return f"{h1:02d}:{m1:02d}"

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "19:34",
    "00:00",
    "11:11",
    "22:22",
    "23:42",
    "23:59",
  ]
  rslts = [solver.nextClosestTime(time) for time in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
