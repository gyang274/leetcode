class LogSystem:

  def __init__(self):
    self.logs = {}

  def timeKey(self, time: List[int]) -> int:
    yy, mn, dd, hh, mm, ss = time
    return (yy - 2000) * 32140800 + (mn - 1) * 2678400 + (dd - 1) * 86400 + hh * 3600 + mm * 60 + ss
    
  def put(self, id: int, timestamp: str) -> None:
    time = [int(x) for x in timestamp.split(":")]
    self.logs[self.timeKey(time)] = id

  def retrieve(self, s: str, e: str, gra: str) -> List[int]:
    s = [int(x) for x in s.split(":")]
    e = [int(x) for x in e.split(":")]
    g = ["Year", "Month", "Day", "Hour", "Minute", "Second"].index(gra)
    r = [(2000, 2017), (1, 12), (1, 31), (0, 23), (0, 59), (0, 59)]
    for i in range(g + 1, 6):
      s[i], e[i] = r[i]
    ks, ke = self.timeKey(s), self.timeKey(e)
    return [v for k, v in self.logs.items() if ks <= k <= ke]

# ["LogSystem","put","put","put","retrieve","retrieve"]
# [[],[1,"2017:01:01:23:59:59"],[2,"2017:01:01:22:59:59"],[3,"2016:01:01:00:00:00"],["2016:01:01:01:01:01","2017:01:01:23:00:00","Year"],["2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"]]
