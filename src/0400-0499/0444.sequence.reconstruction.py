from typing import List
from collections import defaultdict

class Solution:
  def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
    n = len(org)
    if n == 1:
      return len(seqs) > 0 and all([seq == org for seq in seqs])
    # d0: x -> index in org, s0: (org[i], org[i + 1]) in org
    # org[i] and org[i + 1] must be in the same sequence adjancently at once.
    d0, s0 = {}, set([])
    d0[org[0]] = 0
    for k in range(1, n):
      d0[org[k]] = k
      s0.add((org[k - 1], org[k]))
    # if and only if..
    for seq in seqs:
      for i in range(len(seq)):
        if seq[i] not in d0:
          return False
        if i > 0:
          if d0[seq[i - 1]] > d0[seq[i]]:
            return False
          s0.discard((seq[i - 1], seq[i]))
    return s0 == set([])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2], [[1,2],[2,1]]),
    ([1,2,3], [[1,2],[1,3]]),
    ([1,2,3], [[1,2],[2,3]]),
    ([1,2,3], [[1,2],[2,3],[1,3]]),
    ([1,2,3], [[1,2],[2,3],[3,1]]),
    ([4,1,5,2,6,3], [[5,2,6,3],[4,1,5,2]]),
  ]
  rslts = [solver.sequenceReconstruction(org, seqs) for org, seqs in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
        