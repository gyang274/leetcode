from typing import List

class Solution:
  def removeSubfolders(self, folder: List[str]) -> List[str]:
    # key: subfolder are shown after parent folder after sorting.
    ans = set()
    folder.sort()
    for x in folder:
      y, seen = '/', False
      for s in x[1:]:
        if s == '/' and y in ans:
          seen = True
          break
        y += s
      if not seen:
        ans.add(x)
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["/a","/a/b/c","/a/b/d"],
    ["/a","/a/b","/c/d","/c/d/e","/c/f"],
  ]
  rslts = [solver.removeSubfolders(folder) for folder in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
