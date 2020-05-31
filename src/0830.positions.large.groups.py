class Solution:
  def largeGroupPositions(self, S: str) -> List[List[int]]:
    i, l, n = 0, [], len(S)
    for j in range(n):
      if S[j] != S[i]:
        if j - i > 2:
          l.append((i, j - 1))
        i = j
    if j - i > 1:
      l.append((i, j))
    return l
