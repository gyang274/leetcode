from typing import List

class Solution:
  def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
    if 4 * boardingCost <= runningCost:
      return -1
    p, mp, c, mc, w = 0, 0, 0, 0, 0
    for x in customers:
      w += x
      b = min(w, 4)
      w -= b
      p += 4 * boardingCost - runningCost
      c += 1
      if p > mp:
        mc = c
      mp = max(mp, p)
    if w > 0:
      p += (4 * boardingCost - runningCost) * (w // 4)
      c += w // 4
      w %= 4
      mc = c
      mp = max(mp, p)
    if w > 0:
      p += (w * boardingCost - runningCost)
      c += 1
      if p > mp:
        mc = c
      mp = max(mp, p) 
    return mc if mp > 0 else -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([8,3], 5, 6),
  ]
  rslts = [solver.minOperationsMaxProfit(customers, boardingCost, runningCost) for customers, boardingCost, runningCost in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
