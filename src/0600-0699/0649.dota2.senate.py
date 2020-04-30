from collections import deque

class Solution:
  def predictPartyVictory(self, senate: str) -> str:
    """simulation
    """
    # sent: num of live senate on R and D
    # bans: num of bans wait to execute on R and D
    sent, bans = [senate.count("R"), senate.count("D")], [0, 0]
    senate = deque(senate)
    while all(sent):
      # p: party, R or D
      p = senate.popleft() 
      # x: 0 (R) or 1 (D)
      x = p == "D"
      if bans[x] > 0:
        bans[x] -= 1
        sent[x] -= 1
      else:
        bans[x ^ 1] += 1
        senate.append(p)
    return "Radiant" if sent[0] else "Dire"

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "RD",
    "RDD",
    "RRDD",
    "RRDDD",
  ]
  rslts = [solver.predictPartyVictory(senate) for senate in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
