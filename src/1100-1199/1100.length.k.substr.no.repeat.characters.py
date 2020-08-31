from collections import defaultdict

class Solution:
  def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
    if K > 26 or K > len(S):
      return 0
    # O(N) two pointer
    # d: counter of character appearances in length K substr
    # x: num of repeats, if any, in the current length K substr
    # init
    d, x = defaultdict(lambda: 0), 0
    for i in range(K):
      d[S[i]] += 1
      if d[S[i]] > 1:
        x += 1
    count = 1 if x == 0 else 0
    # main
    for i in range(K, len(S)):
      if d[S[i - K]] > 1:
        x -= 1
      d[S[i - K]] -= 1
      d[S[i]] += 1
      if d[S[i]] > 1:
        x += 1
      count += 1 if x == 0 else 0
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("havefunonleetcode", 5),
  ]
  rslts = [solver.numKLenSubstrNoRepeats(S, K) for S, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
