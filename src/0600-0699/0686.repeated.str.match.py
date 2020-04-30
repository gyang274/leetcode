
class Solution:
  def repeatedStringMatch(self, A: str, B: str) -> int:
    """O(N): Rabin-Karp, Rolling Hash.
    """
    return NotImplemented

class Solution:
  def repeatedStringMatch(self, A: str, B: str) -> int:
    q = (len(B) - 1) // len(A) + 1
    for i in range(2):
      if B in A * (q + i):
        return q + i
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("aaac", "aac"),
    ("abcd", "cdabcd"),
    ("abcd", "cdabcdab"),
  ]
  rslts = [solver.repeatedStringMatch(A, B) for A, B in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
