from collections import defaultdict

class Solution:
  def findRotateSteps(self, ring: str, key: str) -> int:
    """dynamic programming, key[1..i] = min_k(key[1..i_k]),
      key[1..i_k] = min_j (key[1..(i-1)_j] + steps[(i-1)_j, i_k]), i_k: character key[i] at position k
    """
    # if len(key) == 0: return 0
    # hash: character s to index(s)
    rr = defaultdict(set)
    for k, s in enumerate(ring):
      rr[s].add(k)
    # steps move from index j to k
    steps = lambda j, k: min((j - k) % len(ring), (k - j) % len(ring))
    # dynamic programming ..
    memo = {}
    for i in range(len(key)):
      memo[i] = {}
      iks = rr[key[i]]
      if i == 0:
        for ik in iks:
          memo[i][ik] = steps(0, ik)
      else:
        im1js = rr[key[i - 1]]
        for ik in iks:
          memo[i][ik] = float("inf")
          for im1j in im1js:
            memo[i][ik] = min(memo[i][ik], memo[i - 1][im1j] + steps(im1j, ik))
    return min(memo[len(key) - 1].values()) + len(key)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("godding", "gd"),
    ("adjfalfdiaoejqdfiaudaierieaikjalkrfi", "fakdj"),
  ]
  rslts = [solver.findRotateSteps(ring, key) for ring, key in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
