from typing import List

class Solution:
  def recursive(self, i, j, k):
    # i, j, k: score of boxes[i:j] with k boxes of boxes[j-1] trailing on right, as a result of knock out boxes[j+].
    if (i, j, k) not in self.memo:
      self.memo[(i, j, k)] = 0
      if i < j:
        # q s.t. (i == q or boxes[q-1] != boxes[q]) and (boxes[r] == boxes[j-1], all q <= r < j)
        q = j
        while i < q and self.boxes[q - 1] == self.boxes[j - 1]:
          q -= 1
        # option: base case, remove trailing boxes all at once
        self.memo[(i, j, k)] = self.recursive(i, q, 0) + (k + (j - q)) ** 2
        for p in range(q - 1, i - 1, -1):
          # option: i <= p < q if boxes[p] == boxes[j-1] and self.boxes[p+1] == self.boxes[j-1]
          # score of boxes[(p+1):q] and then scores of boxes[i:(p+1)] with k + (j - q) trailing
          if self.boxes[p] == self.boxes[q] and not self.boxes[p + 1] == self.boxes[q]:
            self.memo[(i, j, k)] = max(
              self.memo[(i, j, k)], self.recursive(i, p + 1, k + (j - q)) + self.recursive(p + 1, q, 0)
            )
    return self.memo[(i, j, k)]
  def removeBoxes(self, boxes: List[int]) -> int:
    """Q0312.
    """
    self.memo, self.boxes, self.n = {}, boxes, len(boxes)
    self.recursive(0, self.n, 0)
    return self.memo[(0, self.n, 0)]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1, 3, 2, 2, 2, 3, 4, 3, 1],
  ]
  rslts = [solver.removeBoxes(boxes) for boxes in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")