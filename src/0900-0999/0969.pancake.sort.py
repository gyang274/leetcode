from typing import List

class Solution:
  def pancakeSort(self, A: List[int]) -> List[int]:
    # note each time flip to fill the last index, and then it can be leaved.
    n, q, ans = len(A), {x - 1: i for i, x in enumerate(A)}, []
    for i in range(n - 1, -1, -1):
      if q[i] == i:
        continue
      elif q[i] == 0:
        ans.append(i + 1)
        for k in range(i):
          q[k] = i - q[k]
      else:
        j = q[i]
        ans.extend([j + 1, i + 1])
        # pancake flip at index j to move value i from index j to index 0
        # pancake flip at index i to move value i from index 0 to index i
        for k in range(i):
          if q[k] <= j:
            q[k] = i - (j - q[k])
          else:
            q[k] = i - q[k]
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,5,1,4],
  ]
  rslts = [solver.pancakeSort(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
