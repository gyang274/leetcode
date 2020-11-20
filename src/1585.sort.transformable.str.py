from collections import defaultdict

class Solution:
  def isTransformable(self, s: str, t: str) -> bool:
    # TC: O(N), SC: O(N)
    # operation is kind like bubble sort, is transformable iff for each x, 
    # no y, y < x on the left of 1st appearance of x, if so pop and continue.
    # d: digit -> index
    d = defaultdict(list)
    for i, x in reversed(list(enumerate(s))):
      d[int(x)].append(i)
    # modified bubble sort
    for x in map(int, t):
      if not d[x]:
        return False
      # make sure, no y, y < x on left of x 1st shown
      for y in range(x):
        if d[y] and d[y][-1] < d[x][-1]:
          return False
      d[x].pop()
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("0", "1"),
    ("12345", "12435"),
    ("34521", "23415"),
    ("84532", "34852"),
  ]
  rslts = [solver.isTransformable(s, t) for s, t in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
