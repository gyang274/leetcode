class Solution:
  def customSortString(self, S: str, T: str) -> str:
    d, n = {x: i for i, x in enumerate(S)}, len(S)
    return ''.join(map(lambda x: x[1], sorted([(d.get(x, n), x) for i, x in enumerate(T)])))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ('zyx', 'abcxyz'),
  ]
  rslts = [solver.customSortString(S, T) for S, T in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")