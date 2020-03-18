from typing import List

class Solution:
  def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
    """Q0263, Q0264.
    """
    # idx maintains pointers from prime a to nums, such that
    # min(prime[j] x nums[idx[j]]) is the next super ugly num
    idx, nums = [0 for _ in primes], [1 for _ in range(n)]
    for i in range(1, n):
      candidates = []
      for j in range(len(primes)):
        while primes[j] * nums[idx[j]] <= nums[i - 1]:
          idx[j] += 1
        candidates.append(primes[j] * nums[idx[j]])
      nums[i] = min(candidates)
    return nums[-1]

class Solution:
  def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
    """Q0263, Q0264.
      maintain (memorization) intermediate candidate for next, eliminate repeate computation.
    """
    # idx maintains pointers from prime a to nums, such that
    # min(prime[j] x nums[idx[j]]) is the next super ugly num
    idx, candidates, nums = [0 for _ in primes], [x for x in primes], [1 for _ in range(n)]
    for i in range(1, n):
      d = min(candidates)
      nums[i] = d
      # update candidates list, must update all x == xmin, e.g., 2 * 3 = 6 and 3 * 2 = 6.
      k = [j for j, x in enumerate(candidates) if x == d]
      for j in k:
        idx[j] += 1
        candidates[j] = primes[j] * nums[idx[j]]
    return nums[-1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, [2,3,5,7,11]),
    (10, [2,3,5,7,11]),
    (3, [11,23,37,41,43]),
    (42, [11,23,37,41,43]),
    (342, [11,23,37,41,43]),
  ]
  rslts = [solver.nthSuperUglyNumber(n, primes) for n, primes in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")