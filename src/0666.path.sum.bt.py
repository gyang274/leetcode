from typing import List

class Solution:
  def pathSum(self, nums: List[int]) -> int:
    trie, keys = {}, []
    for num in nums:
      d, i, v = num // 100, num // 10 % 10, num % 10
      trie[(d, i)] = v
      keys.append((d, i))
    xsum = 0
    for d, i in keys:
      kl, kr = (d + 1, (i << 1) - 1), (d + 1, i << 1)
      if kl not in trie and kr not in trie:
        xsum += trie[(d, i)]
      else:
        if kl in trie:
          trie[kl] += trie[(d, i)]
        if kr in trie:
          trie[kr] += trie[(d, i)]
    return xsum

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [114, 222],
    [114, 215, 222],
  ]
  rslts = [solver.pathSum(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
