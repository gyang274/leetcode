class Solution:
  def countPrimes(self, n: int) -> int:
    """sieve with set
    """
    nums = set([i for i in range(2, n)])
    for i in range(2, int(n ** 0.5) + 1):
      if i in nums:
        for j in range(i * i, n, i):
          if j in nums:
            nums.remove(j)
    return len(nums)

class Solution:
  def countPrimes(self, n: int) -> int:
    """sieve the list
    """
    # if n < 2:
    #   return 0
    # index i represent value i is prime or not
    nums = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
      if nums[i]:
        for j in range(i * i, n, i):
          nums[j] = False
    count = 0
    for i in range(2, n):
      if nums[i]:
        count += 1
    return count

class Solution:
  def countPrimes(self, n: int) -> int:
    """sieve the list
    """
    if n < 3:
      return 0
    # index i represent value i is prime or not
    nums = [True] * n
    nums[0] = nums[1] = False
    for i in range(2, int(n ** 0.5) + 1):
      if nums[i]:
        nums[i*i::i] = [False] * len(nums[i*i::i])
    return sum(nums)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    0,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34,
    55,
  ]
  rslts = [solver.countPrimes(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  