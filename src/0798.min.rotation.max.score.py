from typing import List

class Solution:
  def bestRotation(self, A: List[int]) -> int:
    n = len(A)
    s = [0] * n
    for i, x in enumerate(A):
      # interval stabbing
      # x is contribute to score when rotated index j = (i - k) % n >= x
      # instead of putting 1 score for each index j, locate the begin and end index and put +1 and -1,
      # and then accumulate all score contributed by each x all at once.
      d = i - x
      if i - x >= 0:
        # x contribute to score when k in [0, i - x], [i + 1, n - 1]
        s[0] += 1
        if d + 1 < n:
          s[d + 1] -= 1
        if i + 1 < n:
          s[i + 1] += 1
      else:
        # x contribute to score when k in [i + 1, n - d]
        s[0] -= 1
        if i + 1 < n:
          s[i + 1] += 1
        if d + 1 < 0:
          s[n + d + 1] -= 1
    # one pass, accumulate the score for each rotate
    k, ik = s[0], 0
    for i in range(1, n):
      s[i] += s[i - 1]
      if s[i] > k:
        k, ik = s[i], i
    return ik

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,4,0],
    [1,3,0,2,4],
    [3,2,1,0,4],
  ]
  rslts = [solver.bestRotation(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
        