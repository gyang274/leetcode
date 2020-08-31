from typing import List

class Solution:
  def longestWPI(self, hours: List[int]) -> int:
    # TC: O(N), SC: O(N), hashmap of score -> 1st seen index
    # ws = list(accumulate(map(lambda x: 1 if x > 8 else -1, hours)))
    # an interval (i, j) inclusive is well-performing interval if ws[j] - ws[i] > 0
    d, s, ms = {0: -1}, 0, 0
    for i, h in enumerate(hours):
      s += 1 if h > 8 else -1
      d.setdefault(s, i)
      if s > 0:
        ms = i + 1
      else:
        ms = max(ms, i - d.get(s - 1, i))
    return ms

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [9,9,6,0,6,6,9],
  ]
  rslts = [solver.longestWPI(hours) for hours in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
