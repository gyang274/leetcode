import collections
from typing import List


class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    """
    Two str are anagrams if and only if their count on each character is the same, key by count to eliminate sort.
    """
    ans = collections.defaultdict(list)
    for s in strs:
      k = [0] * 26
      for c in s:
        k[ord(c) - ord('a')] += 1
      ans[tuple(k)].append(s)
    return ans.values()


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [],
    ["a"],
    ["eat", "tea", "tan", "ate", "nat", "bat"],
  ]
  rslts = [solver.groupAnagrams(strs) for strs in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")