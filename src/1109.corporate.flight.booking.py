from typing import List

class Solution:
  def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
    # key: O(1), each booking update the ans at i - 1 with +k and j with -k, and
    #  update the ans with accumulative sum all at once at the ende, so overall O(N)
    # instead, if +k for all i to j inclusive which could be O(N), overall O(BN)
    ans = [0] * n
    for i, j, k in bookings:
      ans[i - 1] += k
      if j < n:
        ans[j] -= k
    for i in range(1, n):
      ans[i] += ans[i - 1]
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[1,2,10],[2,3,20],[2,5,25]], 5),
  ]
  rslts = [solver.corpFlightBookings(bookings, n) for bookings, n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
