from typing import List

class Solution:
  def findMaximumXOR(self, nums: List[int]) -> int:
    """x ^ 0 = x, x ^ x = 0
    """
    # check from leftmost prefix 11111.. can be achieved?
    L = len(bin(max(nums))) - 2
    xmax = 0
    for i in range(L - 1, -1, -1):
      xmax <<= 1
      # is i-th position 1 from left to right achievable?
      ixor = xmax | 1
      # if p1 ^ p2 = x => p1 ^ p2 ^ p2 = x ^ p2 => p1 = x ^ p2
      prefixes = {num >> i for num in nums}
      xmax |= any(ixor^p in prefixes for p in prefixes)
    return xmax

class Solution:
  def findMaximumXOR(self, nums: List[int]) -> int:
    """Bitwise Trie: https://en.wikipedia.org/wiki/Trie#Bitwise_tries
    """
    # define length L
    L = len(bin(max(nums))) - 2
    # construct bitwise trie
    trie = {}
    xmax = 0
    for num in nums:
      node = trie
      nxor = trie
      ixor = 0
      for bit in bin(num)[2:].zfill(L):
        bit = int(bit)
        # push num into bitwise trie
        if bit not in node:
          node[bit] = {}
        node = node[bit]
        # compute max xor of this num with all previously inserted
        if 1^bit in nxor:
          # if flip of this bit is shown, should go with it..
          nxor = nxor[1^bit]
          ixor = (ixor << 1) | 1
        else:
          nxor = nxor[bit]
          ixor = ixor << 1
      xmax = max(xmax, ixor)
    return xmax

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [3,10,5,25,2,8],
  ]
  rslts = [solver.findMaximumXOR(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")