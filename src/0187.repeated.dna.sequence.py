from typing import List

class Solution:
  def findRepeatedDnaSequences(self, s: str) -> List[str]:
    """Key idea:
      1. Naive slice and hash each L = 10 sequence O((N-L)L) ~= O(NL), expensive when L is large.
      2. Rabin-Karp algorithm, O(N) since constant slice:
          hash DNA sequence with 4-base, h = sum c_i * 4^{L-1-i}, h_next = (h * 4 - c_0 * 4^L) + c_{L+1}
      3. Bitmask: like Rabin-Karp but encode DNA sequence into 2-base, 2 positions each nucleotide.
    """
    n, L = len(s), 10
    if n <= L:
      return []
    # A: 00, C: 01, G: 10, T: 11
    encoder = {
      "A": 0,
      "C": 1,
      "G": 2,
      "T": 3,
    }
    seen, reps = set(), set()
    # construct 1st code
    code = 0
    for i in range(L):
      code <<= 2
      # code += encoder[s[i]]
      code |= encoder[s[i]]
    seen.add(code)
    # construct each code from previous
    for i in range(L, n):
      # shift left 2 positions
      code <<= 2
      # add next code into last 2 positions
      # code += encoder[s[i]]
      code |= encoder[s[i]]
      # unset the first 2 positions
      code &= ~(3 << (2 * L))
      if code in seen:
        reps.add(s[(i - L + 1):(i + 1)])
      seen.add(code)
    return reps

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
  ]
  rslts = [
    solver.findRepeatedDnaSequences(s) for s in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs}, solution: {rs}")
