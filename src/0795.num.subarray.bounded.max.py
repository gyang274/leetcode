from typing import List

class Solution:
  def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
    n = len(A)
    i, count = 0, 0
    while i < n:
      if A[i] > R:
        i += 1
      else:
        j, ks = i, []
        while j < n and A[j] <= R:
          if A[j] >= L:
            ks.append(j - i + 1)
            i = j + 1
          j += 1
        # j == n or A[j] > R
        ks.append(j - i + 1)
        ns = len(ks)
        for ik in range(ns):
          for jk in range(ik + 1, ns):
            count += ks[ik] * ks[jk]
        i = j + 1
    return count

class Solution(object):
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
      # count: num of subarrays where max <= B
      def count(bound):
        ans = cur = 0
        for x in A :
          cur = cur + 1 if x <= bound else 0
          ans += cur
        return ans
      return count(R) - count(L - 1)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,3,5,1,4,1,8,2,3,1,4], 5, 8), 
    
  ]
  rslts = [solver.numSubarrayBoundedMax(A, L, R) for A, L, R in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")

