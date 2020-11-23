from typing import List

class Solution:
  def minOperations(self, logs: List[str]) -> int:
    count = 0
    for x in logs:
      if x == '../':
        count -= 1
      elif x == './':
        count += 0
      else:
        count += 1
      count = max(0, count)
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["d1/","../","../","../"],
    ["d1/","d2/","../","d21/","./"],
    ["d1/","d2/","./","d3/","../","d32/"],
  ]
  rslts = [solver.minOperations(logs) for logs in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
