from typing import List

class Solution:
  def numFriendRequests(self, ages: List[int]) -> int:
    """TC: O(N + A), SC: O(A), revise condition apply on unique age counts.
    no friends iff:
      (1) age[B] <= 0.5 * age[A] + 7
      (2) age[B] > age[A]
      (3) age[B] > 100 && age[A] < 100
    -> friends iff:
      (1) age[A] > 14
      (2) 0.5 * age[A] + 7 < age[B] <= age[A]
    """
    # counts[i]: num of people with age i
    counts = [0] * 121
    for i in ages:
      counts[i] += 1
    # accsum[i]: accumulate sum of counts
    accsum = [0] * 121
    for i in range(15, 121):
      accsum[i] = counts[i] + accsum[i - 1]
    # count friends requests
    requests = 0
    for i in range(15, 121):
      if counts[i] > 0:
        requests += counts[i] * (accsum[i] - accsum[(i >> 1) + 7] - 1)
    return requests

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [16,17,18,19],
    [20,30,100,110,120],
  ]
  rslts = [solver.numFriendRequests(ages) for ages in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
