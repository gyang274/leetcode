from typing import List

import bisect

class Solution:
  def atMostNGivenDigitSet(self, D: List[str], N: int) -> int:
    """Q0788.
    """
    S, N = set(D), str(N)
    K, L = len(D), len(N)
    # num with length 0, .., L - 1
    count = K * (K ** (L - 1) - 1) // (K - 1) if K > 1 else L - 1
    # num with length L
    for i in range(L):
      k = bisect.bisect_right(D, N[i])
      if k > 0:
        if i < L - 1 and N[i] in S:
          count += (k - 1) * (K ** (L - 1 - i))
        else:
          count += k * (K ** (L - 1 - i))
          break
      else:
        break
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["1","2","3","5","8"], 5),
    (["1","2","3","5","8"], 10),
    (["1","2","3","5","8"], 1285),
    (["1","2","3","5","8"], 11285),
    (["1","2","3","5","8"], 143850),
    (["1","2","3","5","8"], 1340850),
  ]
  rslts = [solver.atMostNGivenDigitSet(D, N) for D, N in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
