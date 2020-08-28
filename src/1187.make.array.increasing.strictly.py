from typing import List

class Solution:
  def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
    # TC: O(min(M, N)*N+MlogM), SC: O(min(M, N))
    m, n = len(arr1), len(arr2)
    # sort O(MlogM)
    arr2.sort()
    # maintain a list of (num-of-swaps, last-value, next-to-swap-index-arr2),
    # where the last value should be decrease as the num of swaps is increase
    ss = [(0, arr1[0], 0)]
    if arr2[0] < arr1[0]:
      ss.append((1, arr2[0], 1))
    # O(N) iteration
    for i in range(1, m):
      st = []
      # O(min(M, N))
      for s, x, j in ss:
        if x < arr1[i]:
          if st:
            if s == st[-1][0]:
              if arr1[i] < st[-1][1]:
                st[-1] = (s, arr1[i], j)
            elif s > st[-1][0]:
              if arr1[i] < st[-1][1]:
                st.append((s, arr1[i], j))
          else:
            st.append((s, arr1[i], j))
        # amortized O(1)
        while j < n and arr2[j] <= x:
          j += 1
        if j < n:
          st.append((s + 1, arr2[j], j))
      # since each swap takes at most 1 entry, and at most O(min(M, N)) swap, so SC: O(min(M, N))
      ss = st
    return ss[0][0] if ss else -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,5,3,6,7], [1,3,4,2]),
    ([1,5,3,6,7], [1,3,4,6]),
    ([1,5,3,6,7], [1,3,3,6]),
    ([0,11,6,1,4,3], [5,4,11,10,1,0])
  ]
  rslts = [solver.makeArrayIncreasing(arr1, arr2) for arr1, arr2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
