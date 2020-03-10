from typing import List
from collections import defaultdict, deque

import heapq

class Solution:
  def _insert(self, dsts: List[str], dst: str) -> None:
    """binary search and insert destination to destination list in lexical order.
    """
    l, r = 0, len(dsts)
    while l < r:
      m = l + (r - l) // 2
      if dst < dsts[m]:
        r = m
      else:
        l = m + 1
    dsts.insert(l, dst)
  def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    # construct tickets to src -> dsts
    graph = defaultdict(lambda: deque([]))
    for ticket in tickets:
      # insert dst to src's dsts list
      self._insert(graph[ticket[0]], ticket[1])
    # reconstruct the itinerary w.r.t lexical order
    ans = ['JFK']
    while graph:
      i = -1
      while ans[i] not in graph:
        i -= 1
      # partial path a.k.a circle
      src, path = ans[i], []
      while src in graph:
        path.append(graph[src].popleft())
        if not graph[src]:
          graph.pop(src)
        src = path[-1]
      ans[(len(ans) + i + 1):(len(ans) + i + 1)] = path
    return ans

class Solution:
  def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    """priority queue instead of sorted list.
    """
    graph = defaultdict(list)
    for ticket in tickets:
      # insert dst to src's dsts list
      heapq.heappush(graph[ticket[0]], ticket[1])
    # reconstruct the itinerary w.r.t lexical order
    ans = ['JFK']
    while graph:
      i = -1
      while ans[i] not in graph:
        i -= 1
      # partial path a.k.a circle
      src, path = ans[i], []
      while src in graph:
        path.append(heapq.heappop(graph[src]))
        if not graph[src]:
          graph.pop(src)
        src = path[-1]
      ans[(len(ans) + i + 1):(len(ans) + i + 1)] = path
    return ans 

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]],
    [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
    [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]],
    [
      ["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],
      ["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],
      ["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]
    ],
  ]
  rslts = [solver.findItinerary(tickets) for tickets in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")