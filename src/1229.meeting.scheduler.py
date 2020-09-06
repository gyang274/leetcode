from typing import List

class Solution:
  def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
    slots1.sort()
    slots2.sort()
    i1, i2, n1, n2 = 0, 0, len(slots1), len(slots2)
    while i1 < n1 and i2 < n2:
      s1, e1 = slots1[i1]
      s2, e2 = slots2[i2]
      if s2 > e1:
        i1 += 1
      elif s1 > e2:
        i2 += 1
      elif s2 >= s1:
        # s1 <= s2 <= e1
        if s2 + duration <= min(e1, e2):
          return [s2, s2 + duration]
        else:
          i1 += 1
      else:
        # s2 <= s1 <= e2
        if s1 + duration <= min(e1, e2):
          return [s1, s1 + duration]
        else:
          i2 += 1
    return []

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8),
    ([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 10),
    ([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 12),
  ]
  rslts = [solver.minAvailableDuration(slots1, slots2, duration) for slots1, slots2, duration in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
