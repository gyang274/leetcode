from collections import Counter

class Solution:
  def isPossible(self, nums: List[int]) -> bool:
    stack = [[nums[0]]]
    for x in nums[1:]:
      i = len(stack) - 1
      while i > 0 and x == stack[i][-1]:
        i -= 1  
      if x == stack[i][-1] + 1:
        stack[i].append(x)
      else:
        stack.append([x])
    return all([len(seq) > 2 for seq in stack])

class Solution(object):
  def isPossible(self, nums):
    """greedy approach, pre-allocated tails.
    """
    count = Counter(nums)
    tails = Counter()
    for x in nums:
      if count[x] == 0:
        continue
      elif tails[x] > 0:
        tails[x] -= 1
        tails[x+1] += 1
      elif count[x+1] > 0 and count[x+2] > 0:
        count[x+1] -= 1
        count[x+2] -= 1
        tails[x+3] += 1
      else:
        return False
      count[x] -= 1
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,2,3,3,4,5],
    [1,2,3,4,4,5],
  ]
  rslts = [solver.isPossible(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")