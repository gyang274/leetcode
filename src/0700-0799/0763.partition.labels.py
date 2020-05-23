from typing import List

class Solution:
  def partitionLabels(self, S: str) -> List[int]:
    # hashmap: x -> indexes
    d = {x:i for i, x in enumerate(S)}
    # construct partitions
    i, n, s, ans = 0, len(S), set([]), []
    while i < n:
      s = set([S[i]])
      j = k = i
      while k < n and any([d[x] > k for x in s]):
        k = max([d[x] for x in s])
        s |= set(S[(j + 1):(k + 1)])
        j = k
      ans.append(k - i + 1)
      i = k + 1
    return ans

class Solution:
  def partitionLabels(self, S: str) -> List[int]:
    # hashmap: x -> indexes
    d = {x:i for i, x in enumerate(S)}
    # construct partitions
    j, k, ans = 0, 0, []
    for i, x in enumerate(S):
      j = max(j, d[x])
      if i == j:
        ans.append(j - k + 1)
        k = j + 1
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "ababcbacadefegdehijhklij",
  ]
  rslts = [solver.partitionLabels(S) for S in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
