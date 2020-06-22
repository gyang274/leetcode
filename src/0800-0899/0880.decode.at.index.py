class Solution:
  def decodeAtIndex(self, S: str, K: int) -> str:
    K -= 1
    i, p, q = 0, 0, []
    while i < len(S):
      z = ''
      while i < len(S) and S[i].isalpha():
        z += S[i]
        i += 1
      x = 1
      while i < len(S) and S[i].isdigit():
        x *= int(S[i])
        i += 1
      q.append((p, z, x))
      p = (p + len(z)) * x
      if p > K:
        while q:
          _p, _z, _x = q.pop()
          K %= (_p + len(_z))
          if K >= _p:
            return _z[K - _p]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("a22", 4),
    ("ab23", 5),
    ("a234567899", 1),
    ("leet2code3", 10),
    ("leet2code3awe5some8", 274),
  ]
  rslts = [solver.decodeAtIndex(S, K) for S, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
