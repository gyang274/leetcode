class Solution:
  def maximumSum(self, arr: List[int]) -> int:
    # status machine, Q0121, Q0122, Q0123, Q0188.
    # m0, m1: max with zero or one deletion separately.
    m0, m1, ans = float('-inf'), float('-inf'), float('-inf')
    for x in arr:
      # m1, max of (m1 with this x, m0 without this x - use one deletion, restart with this x itself)
      m1 = max(m1 + x, m0, x)
      # m0, max of (m0 with this x, restart with this x itself - break)
      m0 = max(m0 + x, x)
      # ans: max of ever seen
      ans = max(ans, m1)
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,-2,0,3],
    [8,-1,6,-7,-4,5,-4,7,-6],
  ]
  rslts = [solver.maximumSum(arr) for arr in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
