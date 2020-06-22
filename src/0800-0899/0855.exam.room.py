import heapq

class ExamRoom:
  """TC O(logN) per seat and leave call, using hashMap + priority queue.
  """

  def __init__(self, N: int):
    self.N = N
    # priority queue of segment length among seats available..
    self.queue = []
    # init: dict on seats available as init of segment
    self.dinit = {}
    # ende: dict on seats available as ende of segment
    self.dende = {}
    # initialize the queue
    self.enqueue(0, N - 1)

  def enqueue(self, init: int, ende: int) -> None:
    # priority as segment length after seat taken
    if init == 0 or ende == self.N - 1:
      priority = ende - init
    else:
      priority = (ende - init) // 2
    # create segment object
    segment = [-priority, init, ende, True]
    # push segment into the queue
    heapq.heappush(self.queue, segment)
    # hash segment into dinit and dende for marking True/False as segment valid or not when leave 
    self.dinit[init] = segment
    self.dende[ende] = segment

  def seat(self) -> int:
    # get longest valid segment
    valid = False
    while not valid:
      _, init, ende, valid = heapq.heappop(self.queue)
    self.dinit.pop(init)
    self.dende.pop(ende)
    # s: seat
    s = None
    if init == 0:
      s = init
    elif ende == self.N - 1:
      s = ende
    else:
      s = init + (ende - init) // 2
    # put new segments after seat
    if s - 1 >= init:
      self.enqueue(init, s - 1)
    if s + 1 <= ende:
      self.enqueue(s + 1, ende)
    return s

  def leave(self, p: int) -> None:
    # mark the segments
    init = ende = p
    if p - 1 in self.dende:
      self.dende[p - 1][3] = False
      init = self.dende[p - 1][1]
    if p + 1 in self.dinit:
      self.dinit[p + 1][3] = False
      ende = self.dinit[p + 1][2]
    self.enqueue(init, ende)
