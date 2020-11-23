from functools import lru_cache

class Solution:
  def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
    @lru_cache(None)
    # count the cost of compressing from the i-th index
    def cost(i, x, r, d):
      # i, x, r, d: start index, previous character, running length of the previous character, num of deletions so far.
      if i >= len(s):
        return 0
      if s[i] == x:
        # this is a stretch of the r of the same chars, what is the cost of adding one more? 
        # no need to delete this one, always delete from the beginning one in a stretch of chars like 'aaaaa' to avoid duplication
        return (1 if r == 1 or r == 9 or r == 99 else 0) + cost(i + 1, x, r + 1, d)
      else:
        # keep this char for compression
        # it will increase the result length by 1 plus the cost of compressing the rest of the string 
        c = 1 + cost(i + 1, s[i], 1, d)
        # delete this char for compression
        if d < k:
          c = min(c, cost(i + 1, x, r, d + 1))
        return c
    return cost(0, "", 0, 0)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("aabbaa", 2),
    ("aaabcccd", 2),
    ("aaaaaaaaaaa", 0),
    ("aaaaaaaaaaa", 1),
    ("aaaaaaaaaaa", 2),
  ]
  rslts = [solver.getLengthOfOptimalCompression(s, k) for s, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
