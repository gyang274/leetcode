import itertools

class Solution:
  def kSimilarity(self, A: str, B: str) -> int:
    # compare by index A, B 
    # if a -> b, b -> a then 1 switch
    # if a -> b, b -> c, c -> a then 2 switches
    # ... circle size - 1 switches for each circle
    # so minK = sum of circle sizes - max(num of circles)
    # sum of circle sizes is fixed as total difference
    # max(num of circles) = 1 + max(num of circle of graph removed any circle)
    # dp..
    return NotImplemented

class Solution:
  def kSimilarity(self, A: str, B: str) -> int:
    """Q0839, similar str groups.
    """
    if A == B:
      return 0
    n = len(A)
    queue, seen = [(A, 0)], {A}
    for S, k in queue:
      S = list(S)
      i = 0
      while S[i] == B[i]:
        i += 1
      for j in range(i + 1, n):
        if B[i] == S[j]:
          S[i], S[j] = S[j], S[i]
          T = ''.join(S)
          if T == B:
            return k + 1
          if T not in seen:
            seen.add(T)
            queue.append((T, k + 1))
          S[i], S[j] = S[j], S[i]
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("ab", "ba"),
    ("abacbc", "bccaba"),
    ("abccaacceecdeea", "bcaacceeccdeaae"),
    ("abcdefabcdefabcdef", "edcfbebceafcfdabad"),
  ]
  rslts = [solver.kSimilarity(A, B) for A, B in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")