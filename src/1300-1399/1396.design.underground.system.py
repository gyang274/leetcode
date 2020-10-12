from collections import defaultdict

class UndergroundSystem:

  def __init__(self):
    self.avgTime = defaultdict(lambda: (0, 0))
    self.inTrans = {}

  def checkIn(self, id: int, stationName: str, t: int) -> None:
    self.inTrans[id] = (stationName, t)

  def checkOut(self, id: int, stationName: str, t: int) -> None:
    inStation, inTime = self.inTrans.pop(id)
    prevAvgTime, prevNum = self.avgTime[(inStation, stationName)]
    self.avgTime[(inStation, stationName)] = ((prevAvgTime * prevNum + (t - inTime)) / (prevNum + 1), prevNum + 1)

  def getAverageTime(self, startStation: str, endStation: str) -> float:
    return self.avgTime[(startStation, endStation)][0]
