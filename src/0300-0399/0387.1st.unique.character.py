from collections import defaultdict

class Solution:
  def firstUniqChar(self, s: str) -> int:
    """at most 26 or say O(1) characters.
    """
    # cntr: SC is O(N) this way, but SC can be O(1),
    # make the hashmap character -> (1st-idx, counts)
    cntr = defaultdict(list)
    for i, x in enumerate(s):
      cntr[x].append(i)
    imin = len(s)
    for k, v in cntr.items():
      imin = v[0] if len(v) == 1 and v[0] < imin else imin
    return -1 if imin == len(s) else imin

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "",
    "a",
    "aa",
    "leetcode",
    "helloworld",
    "loveleetcode",
  ]
  rslts = [solver.firstUniqChar(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")