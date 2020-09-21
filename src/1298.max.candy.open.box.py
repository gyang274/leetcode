from typing import List

class Solution:
  def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
    # count the candies after open all possible boxes
    boxes = set(initialBoxes)
    # status as initial set of keys on hand
    bfs = [i for i in boxes if status[i]]
    for i in bfs:
      # collect boxes
      for j in containedBoxes[i]:
        boxes.add(j)
        if status[j]:
          bfs.append(j)
      # collect keys
      for j in keys[i]:
        # open a previously obtained box
        if status[j] == 0 and j in boxes:
          bfs.append(j)
        # use the status to represent keys obtained
        status[j] = 1
    return sum(candies[i] for i in bfs)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,0,1,0], [7,5,4,100], [[],[],[1],[]], [[1,2],[3],[],[]], [0]),
  ]
  rslts = [solver.maxCandies(status, candies, keys, containedBoxes, initialBoxes) for status, candies, keys, containedBoxes, initialBoxes in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
