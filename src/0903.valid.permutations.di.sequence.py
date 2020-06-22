from math import comb

class Solution:
  def __init__(self):
    self.memo = {}
    self.memo[''] = 1
    self.memo['D'] = 1
    self.memo['I'] = 1
  def numPermsDISequence(self, S: str) -> int:
    # let attach -1 on both side of sequence, e.g., -1 + () + -1, 
    # so S will become I + S + D, with length N + 1, then whenever,
    # there is an ID, N can be put and divide the task to left and right.
    if S not in self.memo:
      N, A = len(S), "I" + S + "D"
      self.memo[S] = 0
      for i in range(N + 1):
        if A[i:(i + 2)] == "ID":
          self.memo[S] += comb(N, i) * self.numPermsDISequence(A[1:i]) * self.numPermsDISequence(A[(i + 2):-1])
    return self.memo[S] % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "DIDI",
  ]
  rslts = [solver.numPermsDISequence(S) for S in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
