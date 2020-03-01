from typing import List
from statistics import median

class Solution:
  def wiggleSort(self, nums: List[int]) -> None:
    """Do not return anything, modify nums in-place instead.
      Like Q0075 or Q0280? virtual index mapping x(i), such that if num[x(i)] is sorted then nums wiggle sorted.
      No need of sort, simply if x[i] < x-median for all i <= n//2 and x[j] > x-median for all j >= n//2 + 1 then ok.
      So key is find median in O(N), see median of medians algorithm https://en.wikipedia.org/wiki/median_of_medians.
    refr:
      https://en.wikipedia.org/wiki/dutch_national_flag_problem
    """
    m, n = median(nums), len(nums)
    # x(i) mapping such that if nums[x(i)] is sorted or at least three partitioned (<median, =median, >median)
    # such as in dutch national flag problem, then nums[i] is wiggle sorted as required.
    x = lambda i: (((n - 1) // 2 - i) * 2) if i <= (n - 1) // 2 else (((n - 1) - i) * 2 + 1)
    # print('virtual index mapping x(i):')
    # for i in range(n):
    #   print(f"{i=}, {x(i)=}")
    # numxs[x[i]]
    i, j, k = 0, 0, n - 1
    while j <= k:
      if nums[x(j)] < m:
        # if i < j:
        #   nums[x(i)], nums[x(j)] = nums[x(j)], nums[x(i)]
        nums[x(i)], nums[x(j)] = nums[x(j)], nums[x(i)]
        i += 1
        j += 1
      elif nums[x(j)] > m:
        nums[x(k)], nums[x(j)] = nums[x(j)], nums[x(k)]
        k -= 1
      else:
        # nums[x(j)] == median:
        j += 1
      # print(f'{i=}, {j=}, {k=}, {[nums[x(z) for z in range(n)]]=}')
    return None

class Solution:
  def wiggleSort(self, nums: List[int]) -> None:
    """Do not return anything, modify nums in-place instead.
      Like Q0075 or Q0280? virtual index mapping x(i), such that if num[x(i)] is sorted then nums wiggle sorted.
      No need of sort, simply if x[i] < x-median for all i <= n//2 and x[j] > x-median for all j >= n//2 + 1 then ok.
      So key is find median in O(N), see median of medians algorithm https://en.wikipedia.org/wiki/median_of_medians.
    refr:
      https://en.wikipedia.org/wiki/dutch_national_flag_problem
    """
    m, n = median(nums), len(nums)
    # x(i) mapping such that if nums[x(i)] is reverse sorted or at least three partitioned (<median, =median, >median)
    # such as in dutch national flag problem, then nums[i] is wiggle sorted as required.
    x = lambda i: (2 * i + 1) % (n | 1)
    # print('virtual index mapping x(i):')
    # for i in range(n):
    #   print(f"{i=}, {x(i)=}")
    # numxs[x[i]]
    i, j, k = 0, 0, n - 1
    while j <= k:
      if nums[x(j)] > m:
        # if i < j:
        #   nums[x(i)], nums[x(j)] = nums[x(j)], nums[x(i)]
        nums[x(i)], nums[x(j)] = nums[x(j)], nums[x(i)]
        i += 1
        j += 1
      elif nums[x(j)] < m:
        nums[x(k)], nums[x(j)] = nums[x(j)], nums[x(k)]
        k -= 1
      else:
        # nums[x(j)] == median:
        j += 1
      # print(f'{i=}, {j=}, {k=}, {[nums[x(z) for z in range(n)]]=}')
    return None

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [4,5,5,6],
    [1,3,2,2,3,1],
    [1,5,1,1,6,4],
    [2,4,3,4,5,4,8],
  ]
  rslts = [solver.wiggleSort(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")