from typing import List
from collections import defaultdict

class Solution:
  def findDuplicate(self, paths: List[str]) -> List[List[str]]:
    d = defaultdict(set)
    for path in paths:
      # directory name, filename, filecontent
      root, *fs = path.split()
      for file in fs:
        fn, fc = file[:-1].split("(")
        d[fc].add(root + "/" + fn)
    return [v for k, v in d.items() if len(v) > 1]

# discussion
# BFS vs DFS:
# BFS explores neigbours together, locality, easier to parallelize.
# Large File (GB):
# 1. compare size
# 2. compare hash, e.g., MD5, SHA256
# 3. compare byte to byte to avoid false positive
# vs-code, compare local file with remote server file, synchronize or not.
# Complexity
# TC: O(N^2*L), L is max file size
# SC: O(H^2*L), H is the hash code size, L is the file name size

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(ijkl)"],
  ]
  rslts = [solver.findDuplicate(paths) for paths in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")